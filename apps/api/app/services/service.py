from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
import uuid

from app.models.domain import CropDiagnosticRecord
from app.repositories.domain import CropAdvisoryRepository
from app.schemas.domain import VoiceDiagnosticRequest, VoiceDiagnosticResponse

class CropAdvisoryService:
    def __init__(self, repo: CropAdvisoryRepository):
        self.repo = repo

    async def diagnose_voice_input(self, req: VoiceDiagnosticRequest) -> VoiceDiagnosticResponse:
        is_rust = "ቢጫ" in req.voice_transcript or "rust" in req.voice_transcript.lower()
        diagnosis_str = "Yellow Rust (Puccinia striiformis)" if is_rust else "Early Blight (Alternaria solani)"
        treatment = "Apply Propiconazole fungicide at 0.5L/ha." if is_rust else "Apply Mancozeb 80% WP."
        fertilizer = "Urea: 100 kg/ha, DAP: 50 kg/ha"

        record_id = f"CROP-{uuid.uuid4().hex[:8].upper()}"
        db_obj = CropDiagnosticRecord(
            id=record_id,
            farmer_id=req.farmer_id,
            crop_type=req.crop_type,
            voice_transcript=req.voice_transcript,
            language=req.language,
            diagnosis=diagnosis_str
        )
        saved = await self.repo.create(db_obj)

        return VoiceDiagnosticResponse(
            farmer_id=saved.farmer_id,
            crop_type=saved.crop_type,
            diagnosis=saved.diagnosis,
            confidence=0.94,
            recommended_treatment=treatment,
            recommended_fertilizer=fertilizer,
            diagnosed_at=saved.created_at
        )

    async def list_diagnostics(self, skip: int = 0, limit: int = 50) -> List[CropDiagnosticRecord]:
        return await self.repo.get_multi(skip=skip, limit=limit)
