from pydantic import BaseModel, Field
from typing import Optional, List


class Answer(BaseModel):
    """
    Repräsentiert eine generierte Antwort auf eine Benutzeranfrage.
    Optional können verwendete Quellen angegeben werden (z. B. für Transparenz).
    """

    text: str = Field(..., description="Die vollständige generierte Antwort.")
    sources: Optional[List[str]] = Field(
        default=None,
        description="Optionale Liste der Dokumentquellen oder Chunks, auf die sich die Antwort stützt."
    )

    class Config:
        schema_extra = {
            "example": {
                "text": "Die Leuchte mit der Erzeugnisnummer 4062172212311 ist die OSRAM XBO R 180W/45C.",
                "sources": ["catalog-2023.pdf, Seite 15", "produktdatenblatt.pdf, Seite 2"]
            }
        }
