from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.deps import get_db
from app.repositories.domain import CropAdvisoryRepository
from app.schemas.analytics import CropAdvisoryAnalyticsResponse
from app.services.analytics import CropAdvisoryAnalyticsService

router = APIRouter(prefix="/analytics", tags=["Crop Advisory Analytics"])

@router.get("", response_model=CropAdvisoryAnalyticsResponse)
async def get_analytics(db: AsyncSession = Depends(get_db)):
    repo = CropAdvisoryRepository(db)
    service = CropAdvisoryAnalyticsService(repo)
    return await service.get_crop_analytics()
