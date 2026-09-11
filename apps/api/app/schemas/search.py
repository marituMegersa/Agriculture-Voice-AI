from pydantic import BaseModel, Field
from typing import List, Optional
from app.schemas.domain import VoiceDiagnosticResponse

class CropSearchQuery(BaseModel):
    crop_type: Optional[str] = Field(None, example="Wheat")
    language: Optional[str] = Field(None, example="Amharic")
    page: int = Field(1, ge=1)
    page_size: int = Field(20, ge=1, le=100)

class PaginatedCropResponse(BaseModel):
    items: List[VoiceDiagnosticResponse]
    total: int
    page: int
    page_size: int
    total_pages: int
