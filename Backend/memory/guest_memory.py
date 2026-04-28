# services/guest_memory.py

from langchain_core.messages import HumanMessage, AIMessage

# Global in-memory storage
guest_sessions = {}

# =========================
# Get chat history
# =========================
def get_guest_history(session_id):
    history = guest_sessions.get(session_id, [])

    messages = []

    for item in history:
        if item["role"] == "user":
            messages.append(HumanMessage(content=item["text"]))
        else:
            messages.append(AIMessage(content=item["text"]))

    return messages


# =========================
# Save conversation
# =========================
def save_guest_message(session_id, user_text, ai_text):
    guest_sessions.setdefault(session_id, []).append(
        {"role": "user", "text": user_text}
    )
    guest_sessions[session_id].append(
        {"role": "ai", "text": ai_text}
    )