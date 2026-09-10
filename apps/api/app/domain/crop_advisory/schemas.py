from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime

class CropAdvisoryRequest(BaseModel):

    farmer_id: str
    crop_type: str
    language: Optional[str] = "am"
    symptom_description: str


class CropAdvisoryResponse(BaseModel):
    id: str
    status: str = "COMPLETED"
    summary: str
    confidence_score: float = 0.98
    created_at: datetime

    class Config:
        from_attributes = True
