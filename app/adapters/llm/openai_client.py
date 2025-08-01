from app.core.interfaces.llm_client import LLMClient
from app.core.models.query import Query
from app.core.models.answer import Answer
from openai import OpenAI
from app.config import settings


class OpenAIClient(LLMClient):
    """
    Adapter für das OpenAI API, konform zum LLMClient Interface.
    """

    def __init__(self):
        self.client = OpenAI(api_key=settings.openai_api_key)
        self.model = settings.llm_model_name

    def answer(self, query: Query, context: str) -> Answer:
        """
        Führt eine LLM-Anfrage mit eingebettetem Kontext durch.
        """

        system_prompt = (
            "Du bist ein präziser KI-Experte für technische Produktdaten. "
            "Nutze den gegebenen Kontext, um die Frage zu beantworten. "
            "Wenn du keine Antwort im Kontext findest, sage dies ausdrücklich."
        )

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Kontext:\n{context}\n\nFrage:\n{query.text}"}
        ]

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0.2
        )

        return Answer(text=response.choices[0].message.content.strip())
