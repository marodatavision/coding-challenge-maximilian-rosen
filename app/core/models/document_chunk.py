from pydantic import BaseModel, Field
from typing import Optional, Dict


class DocumentChunk(BaseModel):
    """
    Repräsentiert einen extrahierten und ggf. gesplitteten Abschnitt (Chunk) aus einem PDF-Dokument.
    Wird verwendet für das Einbetten, Speichern in der Vektordatenbank und das Retrieval.
    """

    text: str = Field(..., description="Der reine Textinhalt dieses Chunks.")
    metadata: Optional[Dict[str, str]] = Field(
        default_factory=dict,
        description="Zusätzliche Metadaten wie Seitenzahl, Quelle etc.",
    )

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "text": "SIRIUS HRI 330W bietet eine Lebensdauer von 1500 Stunden.",
                "metadata": {"source": "catalog-2023.pdf", "page": "23"},
            }
        }
