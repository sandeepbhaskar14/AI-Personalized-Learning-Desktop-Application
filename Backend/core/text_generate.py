import os, time

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
active_streams = {}


def stream_ai_response(
    prompt, chat_id, text, task, difficulty, style,
    document_text=None,
    document_name=None,
    document_image_b64=None,
    document_image_mime="image/png",
):
    """
    Stream an AI response to the client.
 
    Parameters
    ----------
    prompt               : Prompt ORM object (None for guests)
    chat_id              : str
    text                 : The user's question / prompt text
    task                 : prompt_type (search, summary, mcqs, …)
    difficulty           : e.g. "easy" / "medium" / "hard"
    style                : learning style e.g. "text" / "visual"
    document_text        : Optional extracted text from a document file
    document_name        : Optional filename of the attachment
    document_image_b64   : Optional base64-encoded image bytes (for vision)
    document_image_mime  : MIME type of the image, e.g. "image/png"
    """
    active_streams[chat_id] = False  # False = keep going
    
    def generate():
        full_text = ""
        start_time = time.time()

        # ── Conversation history ───────────────────────────────────────
        messages = (get_chat_history(chat_id) if prompt
                    else get_guest_history(chat_id))

        # ── System prompt ──────────────────────────────────────────────
        system_prompt = (
            "Always format code using triple backticks with language.\n"
            f"You are a personalized learning assistant.\n"
            f"Task: {task}\n"
            f"Difficulty: {difficulty}\n"
            f"Style: {style}"
        )
 
        # Inject the document as grounded context when present
        if document_text:
            doc_label = f'"{document_name}"' if document_name else "the uploaded document"
            system_prompt += (
                f"\n\nThe user has uploaded a document ({doc_label}). "
                "Its content is provided below between the <document> tags. "
                "Use it as the primary source when answering. "
                "Quote or reference specific parts where helpful. "
                "If the answer cannot be found in the document, say so clearly "
                "before drawing on your general knowledge.\n\n"
                f"<document>\n{document_text}\n</document>"
            )

        messages.insert(0, SystemMessage(content=system_prompt))
        
        # ── Build the final HumanMessage ──────────────────────────────
        # If a base64 image was provided, send a multimodal content block
        # so the vision model can actually see the pixels.
        if document_image_b64:
            image_url = f"data:{document_image_mime};base64,{document_image_b64}"
            human_content = [
                {
                    "type": "image_url",
                    "image_url": {"url": image_url},
                },
                {
                    "type": "text",
                    "text": text,
                },
            ]
            messages.append(HumanMessage(content=human_content))
        else:
            messages.append(HumanMessage(content=text))

        # ── Stream tokens ──────────────────────────────────────────────
        for chunk in llm.stream(messages):
            if active_streams.get(chat_id, False):
                active_streams.pop(chat_id, None)
                break 
            
            token = chunk.content
            if token:
                full_text += token
                yield token.replace("\n", "<<NEWLINE>>") + "\n"
                
        # Cleanup stop flag
        active_streams.pop(chat_id, None)
        
        # ── Persist to DB (logged-in users only) ───────────────────────
        if prompt: 
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