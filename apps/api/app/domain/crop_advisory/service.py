from sqlalchemy.orm import Session
from typing import List
import uuid
from app.domain.crop_advisory.models import CropDiagnosticRecord
from app.domain.crop_advisory.schemas import VoiceDiagnosticRequest, VoiceDiagnosticResponse
from app.domain.crop_advisory.engine import CropDiagnosticEngine

class CropAdvisoryService:
    @staticmethod
    def diagnose_and_store(db: Session, req: VoiceDiagnosticRequest) -> VoiceDiagnosticResponse:
        res = CropDiagnosticEngine.diagnose_transcript(
            transcript=req.voice_transcript,
            crop_type=req.crop_type,
            language=req.language
        )
        
        record_id = f"CROP-{uuid.uuid4().hex[:8].upper()}"
        db_obj = CropDiagnosticRecord(
            id=record_id,
            farmer_id=req.farmer_id,
            crop_type=req.crop_type,
            voice_transcript=req.voice_transcript,
            language=req.language,
            diagnosis=res["diagnosis"]
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        
        return VoiceDiagnosticResponse(
            farmer_id=db_obj.farmer_id,
            crop_type=db_obj.crop_type,
            diagnosis=db_obj.diagnosis,
            confidence=res["confidence"],
            recommended_treatment=res["recommended_treatment"],
            recommended_fertilizer=res["recommended_fertilizer"],
            diagnosed_at=db_obj.created_at
        )

    @staticmethod
    def list_diagnostics(db: Session, skip: int = 0, limit: int = 50) -> List[CropDiagnosticRecord]:
        return db.query(CropDiagnosticRecord).offset(skip).limit(limit).all()
