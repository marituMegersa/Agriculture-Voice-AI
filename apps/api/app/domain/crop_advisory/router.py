from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domain.crop_advisory.schemas import VoiceDiagnosticRequest, VoiceDiagnosticResponse
from app.domain.crop_advisory.service import CropAdvisoryService

router = APIRouter(prefix="/api/v1/crop_advisory", tags=["Crop Advisory & Soil Diagnostics"])

@router.post("/diagnose", response_model=VoiceDiagnosticResponse, status_code=status.HTTP_201_CREATED)
def diagnose_crop_voice(req: VoiceDiagnosticRequest, db: Session = Depends(get_db)):
    return CropAdvisoryService.diagnose_and_store(db, req)

@router.get("/history")
def list_diagnostics(skip: int = Query(0, ge=0), limit: int = Query(50, le=100), db: Session = Depends(get_db)):
    return CropAdvisoryService.list_diagnostics(db, skip=skip, limit=limit)
