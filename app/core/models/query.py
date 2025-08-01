from pydantic import BaseModel, Field


class Query(BaseModel):
    """
    Repräsentiert eine Benutzeranfrage, die an das RAG-System gestellt wird.
    Wird in der Query-Pipeline verwendet zur Validierung und Weiterverarbeitung.
    """

    text: str = Field(..., description="Die ursprüngliche Frage des Nutzers.")

    class Config:
        schema_extra = {
            "example": {
                "text": "Welche Leuchte hat die primäre Erzeugnisnummer 4062172212311?"
            }
        }
