from langchain_core.callbacks import BaseCallbackHandler

class StreamingHandler(BaseCallbackHandler):
    def __init__(self):
        self.tokens = []

    def on_llm_new_token(self, token, **kwargs):
        self.tokens.append(token)