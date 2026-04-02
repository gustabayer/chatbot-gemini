from google import genai
from src.config import GEMINI_API_KEY
from src.prompts import SYSTEM_PROMPT


class EsportsChatbot:
    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)
        self.model = "gemini-2.5-flash"

    def responder(self, pergunta: str) -> str:
        resposta = self.client.models.generate_content(
            model=self.model,
            contents=f"{SYSTEM_PROMPT}\n\nPergunta do usuário: {pergunta}"
        )
        return resposta.text.strip()