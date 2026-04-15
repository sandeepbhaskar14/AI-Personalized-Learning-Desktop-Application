# routes/process_prompts.py

import time
import datetime
from flask import request, jsonify
# from flask_jwt_extended import jwt_required, get_jwt_identity

from models import Prompt, UserPreferences
from main import app, db, verify_token

import uuid

# Import AI service
from text_generate import stream_ai_response

@app.route("/prompt/stream", methods=["POST"])
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