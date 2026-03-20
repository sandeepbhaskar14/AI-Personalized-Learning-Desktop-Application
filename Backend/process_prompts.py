import time
from models import Result, Prompt
from main import *

def generate_response(text, task, difficulty, style):
    if task == "summary":
        return f"[SUMMARY - {difficulty.upper()}]\n{text[:200]}..."

    if task == "quiz":
        return f"[QUIZ]\n1. What is {text.split()[0]}?\nA) ..."

    if task == "flashcards":
        return f"[FLASHCARDS]\nQ: {text}\nA: Explanation"

    if task == "explain":
        return f"[EXPLANATION - {style.upper()}]\n{text}"

    return "Task not supported"

@app.route("/prompt", methods=["POST"])
def handle_prompt():
    user_id, error_response, status_code = verify_token()
    data = request.json

    prompt_text = data.get("prompt_text")
    prompt_type = data.get("prompt_type")

    if not prompt_text or not prompt_type:
        return jsonify({"error": "Invalid input", "status_code": 400})

    # 1. Create prompt with PENDING status
    prompt = Prompt(
        user_id=user_id,
        prompt_text=prompt_text,
        prompt_type=prompt_type,
        status="processing",
        created_at=datetime.datetime.utcnow()
    )
    db.session.add(prompt)
    db.session.commit()

    # 2. Start timing
    start_time = time.time()

    try:
        # 3. Fetch preferences
        prefs = UserPreferences.query.filter_by(user_id=user_id).first()

        # 4. Generate response (rule-based for now)
        result_text = generate_response(
            prompt_text,
            prompt_type,
            prefs.difficulty_level,
            prefs.learning_style
        )

        processing_time_ms = int((time.time() - start_time) * 1000)

        # 5. Store response
        response = Result(
            prompt_id=prompt.id,
            result_text=result_text,
            confidence_score=0.75,              # temp heuristic
            processing_time_ms=processing_time_ms,
            model_used="rule_based_v1"
        )

        # 6. Update prompt status
        prompt.status = "completed"

        db.session.add(response)
        db.session.commit()

        return jsonify({
            "prompt_id": prompt.id,
            "status": prompt.status,
            "output": result_text,
            "confidence": response.confidence_score,
            "time_ms": processing_time_ms,
            "status_code": 200
        })

    except Exception as e:
        prompt.status = "failed"
        db.session.commit()

        return jsonify({"error": "Processing failed", "status_code": 500})