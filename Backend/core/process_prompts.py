# routes/process_prompts.py

import datetime, uuid
from flask import request, jsonify, Blueprint

from models.user_models import db, Prompt, UserPreferences, Chat
from services.auth_service import verify_token
from core.text_generate import stream_ai_response, active_streams

chat_bp = Blueprint("chat", __name__)


@chat_bp.route("/chat", methods=["GET"])
def get_chats():
    user_id, error_response, status_code = verify_token()
    if status_code in (401, 403):
        return jsonify({"message": "Unauthorized", "status_code": status_code})
    
    chats = (Chat.query
             .filter_by(user_id=user_id)
             .order_by(Chat.updated_at.desc())
             .limit(50).all())
    
    return jsonify({
        "status_code": 200,
        "chats": [
            {
                "chat_id": c.chat_id,
                "title": c.title,
                "updated_at": c.updated_at.isoformat() if c.updated_at else c.created_at.isoformat()
            }
            for c in chats
        ]
    })


@chat_bp.route("/chat/<chat_id>", methods=["GET"])
def get_chat_messages(chat_id):
    user_id, error_response, status_code = verify_token()
    if status_code in (401, 403):
        return jsonify({"message": "Unauthorized", "status_code": status_code})

    # Verify this chat belongs to the user
    chat = Chat.query.filter_by(chat_id=chat_id, user_id=user_id).first()
    if not chat:
        return jsonify({"message": "Chat not found", "status_code": 404})

    prompts = (
        Prompt.query
        .filter_by(chat_id=chat_id, user_id=user_id)
        .order_by(Prompt.created_at.asc())
        .all()
    )

    messages = []
    for p in prompts:
        # ── user message ──────────────────────────────────────────────────────
        # Include document_name so the frontend can re-render the chip.
        user_msg = {
            "role": "user",
            "text": p.prompt_text,
        }
        if p.document_name:                    # attach filename if saved
            user_msg["document_name"] = p.document_name
 
        messages.append(user_msg)
 
        # ── AI response ───────────────────────────────────────────────────────
        if p.response:
            messages.append({"role": "ai", "text": p.response.result_text})

    return jsonify({
        "status_code": 200,
        "chat_id": chat_id,
        "title": chat.title,
        "messages": messages
    })

@chat_bp.route("/prompt/stop", methods=["POST"])
def stop_prompt():
    data = request.json
    chat_id = data.get("chat_id")
    if chat_id and chat_id in active_streams:
        active_streams[chat_id] = True  # signal the generator to stop
        return jsonify({"message": "Stop signal sent", "status_code": 200})
    return jsonify({"message": "No active stream found", "status_code": 404})

@chat_bp.route("/prompt/stream", methods=["POST"])
def stream_prompt():
    user_id = None
    if request.headers:
        user_id, _, status_code = verify_token()
 
    data = request.json
 
    prompt_text  = data.get("prompt_text")
    prompt_type  = data.get("prompt_type")
    chat_id      = data.get("chat_id") or str(uuid.uuid4())
 
    # ── Document / image fields (all optional) ─────────────────────────
    document_text      = data.get("document_text")       # extracted text
    document_name      = data.get("document_name")       # filename
    document_image_b64 = data.get("document_image_b64")  # base64-encoded image
    document_image_mime= data.get("document_image_mime", "image/png")
 
    if not prompt_text or not prompt_type:
        return jsonify({"error": "Invalid input"}), 400
 
    difficulty     = "medium"
    learning_style = "text"
 
    # ── Logged-in user ─────────────────────────────────────────────────
    if user_id:
        chat = Chat.query.filter_by(chat_id=chat_id).first()
        if not chat:
            chat = Chat(user_id=user_id, chat_id=chat_id,
                        title=prompt_text[:50])
            db.session.add(chat)
        else:
            chat.updated_at = datetime.datetime.utcnow()
        db.session.commit()
 
        prompt = Prompt(
            user_id=user_id, chat_id=chat_id,
            prompt_text=prompt_text, prompt_type=prompt_type,
            status="processing", document_name=document_name,
            created_at=datetime.datetime.utcnow()
        )
        db.session.add(prompt)
        db.session.commit()
 
        prefs = UserPreferences.query.filter_by(user_id=user_id).first()
        if prefs:
            difficulty     = prefs.difficulty_level
            learning_style = prefs.learning_style
        else:
            return jsonify({"error": "User preferences not set"}), 400
    else:
        prompt = None
 
    # ── Stream ─────────────────────────────────────────────────────────
    return stream_ai_response(
        prompt, chat_id, prompt_text,
        prompt_type, difficulty, learning_style,
        document_text=document_text,
        document_name=document_name,
        document_image_b64=document_image_b64,
        document_image_mime=document_image_mime,
    )    
    
@chat_bp.route("/chat/<chat_id>", methods=["DELETE"])
def delete_chat(chat_id):
    user_id, error_response, status_code = verify_token()
    if status_code in (401, 403):
        return jsonify({"message": "Unauthorized", "status_code": status_code})

    chat = Chat.query.filter_by(chat_id=chat_id, user_id=user_id).first()
    if not chat:
        return jsonify({"message": "Chat not found", "status_code": 404})

    # Delete all prompts (and their responses via cascade) for this chat
    prompts = Prompt.query.filter_by(chat_id=chat_id, user_id=user_id).all()
    for prompt in prompts:
        db.session.delete(prompt)

    db.session.delete(chat)
    db.session.commit()

    return jsonify({"message": "Chat deleted", "status_code": 200})


@chat_bp.route("/chat/<chat_id>", methods=["PATCH"])
def rename_chat(chat_id):
    user_id, error_response, status_code = verify_token()
    if status_code in (401, 403):
        return jsonify({"message": "Unauthorized", "status_code": status_code})

    chat = Chat.query.filter_by(chat_id=chat_id, user_id=user_id).first()
    if not chat:
        return jsonify({"message": "Chat not found", "status_code": 404})

    data = request.json
    new_title = data.get("title", "").strip()
    if not new_title:
        return jsonify({"message": "Title cannot be empty", "status_code": 400})

    chat.title = new_title[:100]
    db.session.commit()

    return jsonify({"message": "Chat renamed", "status_code": 200})