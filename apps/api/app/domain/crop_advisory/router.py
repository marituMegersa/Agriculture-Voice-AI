from fastapi import APIRouter
from app.domain.crop_advisory.schemas import VoiceDiagnosticRequest, VoiceDiagnosticResponse
from app.domain.crop_advisory.service import CropAdvisoryService

router = APIRouter(prefix="/api/v1/crop_advisory", tags=["Crop Advisory & Soil Diagnostics"])

@router.post("/diagnose", response_model=VoiceDiagnosticResponse)
def diagnose_voice(req: VoiceDiagnosticRequest):
    return CropAdvisoryService.diagnose_voice_input(req)
