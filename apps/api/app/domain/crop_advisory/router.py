from fastapi import APIRouter, status
from pydantic import BaseModel
from typing import Optional
from app.domain.crop_advisory.service import CropAdvisoryService

router = APIRouter(prefix="/api/v1/crop_advisory", tags=["Crop Advisory"])

class CropInput(BaseModel):
    farmer_id: str
    crop_type: str
    symptom_description: str
    language: Optional[str] = "am"

@router.post("/diagnose", status_code=status.HTTP_200_OK)
def diagnose_crop(data: CropInput):
    return CropAdvisoryService.diagnose_crop(data.farmer_id, data.crop_type, data.symptom_description, data.language)
