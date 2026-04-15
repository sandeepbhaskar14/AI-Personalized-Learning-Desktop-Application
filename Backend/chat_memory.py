from models import Prompt
from langchain_core.messages import HumanMessage, AIMessage
import tiktoken

# 🔧 Config
MAX_MESSAGES = 10
MAX_TOKENS = 1500   # safe for gpt-4o-mini

# Tokenizer
encoding = tiktoken.encoding_for_model("gpt-4o-mini")


def count_tokens(messages):
    total_tokens = 0

    for msg in messages:
        total_tokens += len(encoding.encode(msg.content))

    return total_tokens


def get_chat_history(chat_id):
    prompts = (
        Prompt.query
        .filter_by(chat_id=chat_id)
        .order_by(Prompt.created_at.desc())
        .limit(MAX_MESSAGES)
        .all()
    )

    prompts.reverse()  # oldest → newest

    messages = []

    for prompt in prompts:
        messages.append(HumanMessage(content=prompt.prompt_text))

        if prompt.response:
            messages.append(AIMessage(content=prompt.response.result_text))

    # 🔥 Token trimming
    while count_tokens(messages) > MAX_TOKENS and len(messages) > 2:
        messages.pop(0)  # remove oldest message

    return messages