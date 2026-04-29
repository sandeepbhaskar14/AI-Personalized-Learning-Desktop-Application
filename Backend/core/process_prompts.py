# routes/process_prompts.py

import time
import datetime
from flask import request, jsonify, Blueprint
# from flask_jwt_extended import jwt_required, get_jwt_identity

from models.user_models import db, Prompt, UserPreferences, Chat
from services.auth_service import verify_token

import uuid

# Import AI service
from core.text_generate import stream_ai_response, active_streams


chat_bp = Blueprint("chat", __name__)

@chat_bp.route("/chat", methods=["GET"])
def get_chats():
    user_id, error_response, status_code = verify_token()
    if status_code in (401, 403):
        return jsonify({"message": "Unauthorized", "status_code": status_code})

    chats = (
        Chat.query
        .filter_by(user_id=user_id)
        .order_by(Chat.updated_at.desc())
        .limit(50)
        .all()
    )

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
        messages.append({"role": "user", "text": p.prompt_text})
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
    if request.headers: # user logged in
        user_id, error_response, status_code = verify_token()
        
    data = request.json

    prompt_text = data.get("prompt_text")
    prompt_type = data.get("prompt_type")
    chat_id = data.get("chat_id")

    if not prompt_text or not prompt_type:
        return jsonify({"error": "Invalid input"}), 400

    if not chat_id:
        chat_id = str(uuid.uuid4())
        
    # DEFAULT VALUES (for guest)
    difficulty = "medium"
    learning_style = "text"

    # ===============================
    # LOGGED-IN USER FLOW
    # ===============================
    if user_id:
        # create chat if new
        chat = Chat.query.filter_by(chat_id=chat_id).first()
        if not chat:
            chat = Chat(
                user_id=user_id,
                chat_id=chat_id,
                title=prompt_text[:50]  # first message as title
            )
            db.session.add(chat)
        else:
            chat.updated_at = datetime.datetime.utcnow()

        db.session.commit()
        
        # Create prompt
        prompt = Prompt(
            user_id=user_id,
            chat_id=chat_id,
            prompt_text=prompt_text,
            prompt_type=prompt_type,
            status="processing",
            created_at=datetime.datetime.utcnow()
        )
        db.session.add(prompt)
        db.session.commit()

        prefs = UserPreferences.query.filter_by(user_id=user_id).first()
        if prefs:
            difficulty = prefs.difficulty_level
            learning_style = prefs.learning_style
        else:
            return jsonify({"error": "User preferences not set"}), 400
        
    # ===============================
    # GUEST USER FLOW
    # ===============================
    else:
        prompt = None  # No DB storage

    # ===============================
    # STREAM RESPONSE (COMMON)
    # ===============================

    # STREAM RESPONSE
    return stream_ai_response(
        prompt,
        chat_id,
        prompt_text,
        prompt_type,
        difficulty,
        learning_style
    )
    # except Exception as e:
    #     prompt.status = "failed"
    #     db.session.commit()

    #     return jsonify({"error": str(e), "status_code": 500})