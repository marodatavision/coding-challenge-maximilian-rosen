from pydantic import BaseModel, Field
from typing import Any, Dict

class Document(BaseModel):
    text: str = Field(..., description="Reiner extrahierter Textinhalt des Dokuments")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Metadaten wie Quelle, Titel usw.")
