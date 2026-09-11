from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class VoiceDiagnosticRequest(BaseModel):
    farmer_id: str = Field(..., example="FARMER-8831")
    crop_type: str = Field(..., example="Wheat")
    voice_transcript: str = Field(..., example="እህሌ ቢጫ ዝገት ምልክት አሳይቷል")
    language: str = Field("Amharic", example="Amharic")

class VoiceDiagnosticResponse(BaseModel):
    farmer_id: str
    crop_type: str
    diagnosis: str
    confidence: float
    recommended_treatment: str
    recommended_fertilizer: str
    diagnosed_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        from_attributes = True
