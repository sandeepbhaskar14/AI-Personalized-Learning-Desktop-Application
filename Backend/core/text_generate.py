import os
import time

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

from models.user_models import db
from models.user_models import Response as DBResponse

from flask import Response, stream_with_context
from memory.chat_memory import get_chat_history
from memory.guest_memory import get_guest_history, save_guest_message, guest_sessions
from core.stream_handler import StreamingHandler


load_dotenv()

# Initialize LLM once (important)
llm = ChatOpenAI(
    model="openai/gpt-4o-mini",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    temperature=0.7,
    model_kwargs={
        "extra_body":{
            "reasoning":{
                "enabled":True
            }
        }
    },
    streaming=True
)

# active streams registry: chat_id -> stop_flag (True = stop)
# PROMPTS
active_streams = {}
# -------------------------------


def stream_ai_response(prompt, chat_id, text, task, difficulty, style,
                       document_text=None, document_name=None):
    """
    Stream an AI response to the client.
    Parameters
    ----------
    prompt        : Prompt ORM object (None for guests)
    chat_id       : str
    text          : The user's question / prompt text
    task          : prompt_type (search, summary, mcqs, …)
    difficulty    : e.g. "easy" / "medium" / "hard"
    style         : learning style e.g. "text" / "visual"
    document_text : Optional raw text extracted from an uploaded document
    document_name : Optional filename of the uploaded document
    """
    active_streams[chat_id] = False  # False = keep going
    def generate():
        handler = StreamingHandler()
        full_text = ""
        start_time = time.time()

        # ── Conversation history ───────────────────────────────────────
        if prompt:  # logged-in user
            messages = get_chat_history(chat_id)
        else:       # guest user
            messages = get_guest_history(chat_id)

        # ── System prompt ──────────────────────────────────────────────
        system_prompt = f"""Always format code using triple backticks with language.
            You are a personalized learning assistant.
            Task: {task}
            Difficulty: {difficulty}
            Style: {style}"""
 
        # Inject the document as grounded context when present
        if document_text:
            doc_label = f'"{document_name}"' if document_name else "the uploaded document"
            system_prompt += f"""
 
            The user has uploaded a document ({doc_label}). Its content is provided below between
            the <document> tags. Use it as the primary source when answering the user's question.
            Quote or reference specific parts where helpful. If the answer cannot be found in the
            document, say so clearly before drawing on your general knowledge.
            
            <document>
            {document_text}
            </document>"""



        messages.insert(0, SystemMessage(content=system_prompt))
        messages.append(HumanMessage(content=text))

        # ── Stream tokens ──────────────────────────────────────────────
        for chunk in llm.stream(messages):
            if active_streams.get(chat_id, False):
                active_streams.pop(chat_id, None)
                break  # Stop yielding
            
            token = chunk.content
            if token:
                full_text += token
                encoded = token.replace("\n", "<<NEWLINE>>")
                yield encoded + "\n"
                
        # Cleanup stop flag
        active_streams.pop(chat_id, None)
        
        # ── Persist to DB (logged-in users only) ───────────────────────
        if prompt: # user logged in
            # AFTER STREAM COMPLETE → SAVE DB
            response = DBResponse(
                prompt_id=prompt.id,
                result_text=full_text,
                confidence_score=0.9,
                processing_time_ms=int((time.time() - start_time) * 1000),
                model_used=llm.model_name
            )

            prompt.status = "completed"

            db.session.add(response)
            db.session.commit()
        else:
            # guest mode — keep only the last 10 turns
            save_guest_message(chat_id, text, full_text)
            guest_sessions[chat_id] = guest_sessions[chat_id][-10:]

    return Response(
    stream_with_context(generate()),
    content_type="text/plain",
    headers={
        "Cache-Control": "no-cache",
        "X-Accel-Buffering": "no"
    }
)