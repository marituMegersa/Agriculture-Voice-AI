from sqlalchemy.orm import Session
import uuid
import datetime
from app.domain.crop_advisory.models import CropAdvisoryRecord
from app.domain.crop_advisory.schemas import CropAdvisoryRequest

class CropAdvisoryService:
    @staticmethod
    def process_encounter(db: Session, data: CropAdvisoryRequest) -> CropAdvisoryRecord:
        rec_id = f"REC-{uuid.uuid4().hex[:8]}"
        db_obj = CropAdvisoryRecord(
            id=rec_id,
            created_at=datetime.datetime.utcnow()
        )
        return db_obj
