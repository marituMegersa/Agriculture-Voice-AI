from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional
from app.api.deps import get_db
from app.repositories.domain import CropAdvisoryRepository
from app.schemas.search import PaginatedCropResponse, VoiceDiagnosticResponse

router = APIRouter(prefix="/search", tags=["Search & Filter"])

@router.get("", response_model=PaginatedCropResponse)
async def search_diagnostics(
    crop_type: Optional[str] = Query(None),
    language: Optional[str] = Query(None),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db)
):
    repo = CropAdvisoryRepository(db)
    all_recs = await repo.get_multi(skip=(page - 1) * page_size, limit=page_size)
    items = [
        VoiceDiagnosticResponse(
            farmer_id=r.farmer_id,
            crop_type=r.crop_type,
            diagnosis=r.diagnosis,
            confidence=0.95,
            recommended_treatment="Apply Propiconazole fungicide.",
            recommended_fertilizer="Urea 100kg/ha",
            diagnosed_at=r.created_at
        ) for r in all_recs
    ]
    return PaginatedCropResponse(
        items=items,
        total=len(items),
        page=page,
        page_size=page_size,
        total_pages=1
    )
