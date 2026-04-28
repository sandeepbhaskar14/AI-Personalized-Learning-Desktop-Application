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
    api_key="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",
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


#  Secure config
# llm = ChatOpenAI(
#     model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
#     api_key=os.getenv("OPENAI_API_KEY"),
#     temperature=0.7
# )

# -------------------------------
# PROMPTS
# -------------------------------

active_streams = {}  # chat_id -> stop_flag

def stream_ai_response(prompt, chat_id, text, task, difficulty, style):
    active_streams[chat_id] = False  # False = keep going
    def generate():
        handler = StreamingHandler()
        full_text = ""
        start_time = time.time()

        if prompt:  # logged-in user
            messages = get_chat_history(chat_id)
        else:       # guest user
            messages = get_guest_history(chat_id)

        system_prompt = f"""
        Always format code using triple backticks with language.
        You are a personalized learning assistant.
        Task: {task}
        Difficulty: {difficulty}
        Style: {style}
        """

        messages.insert(0, SystemMessage(content=system_prompt))
        messages.append(HumanMessage(content=text))

        for chunk in llm.stream(messages):
            if active_streams.get(chat_id, False):
                active_streams.pop(chat_id, None)
                break  # Stop yielding
            
            token = chunk.content
            if token:
                full_text += token
                encoded = token.replace("\n", "<<NEWLINE>>")
                yield encoded + "\n"
                
        # Cleanup flag
        active_streams.pop(chat_id, None)
        
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
            # guest mode
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