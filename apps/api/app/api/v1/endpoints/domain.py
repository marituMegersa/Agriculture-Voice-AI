from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.api.deps import get_db
from app.schemas.domain import VoiceDiagnosticRequest, VoiceDiagnosticResponse
from app.repositories.domain import CropAdvisoryRepository
from app.services.domain import CropAdvisoryService

router = APIRouter(prefix="/crop_advisory", tags=["Crop Advisory & Soil Diagnostics"])

def get_service(db: AsyncSession = Depends(get_db)) -> CropAdvisoryService:
    repo = CropAdvisoryRepository(db)
    return CropAdvisoryService(repo)

@router.post("/diagnose", response_model=VoiceDiagnosticResponse, status_code=status.HTTP_201_CREATED)
async def diagnose_crop(req: VoiceDiagnosticRequest, service: CropAdvisoryService = Depends(get_service)):
    return await service.diagnose_voice_input(req)

@router.get("/history")
async def list_diagnostics(skip: int = Query(0, ge=0), limit: int = Query(50, le=100), service: CropAdvisoryService = Depends(get_service)):
    return await service.list_diagnostics(skip=skip, limit=limit)
