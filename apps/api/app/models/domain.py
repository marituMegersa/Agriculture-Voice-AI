from sqlalchemy import Column, String, DateTime, Float, JSON
import datetime
from app.core.database import Base

class CropDiagnosticRecord(Base):
    __tablename__ = "crop_diagnostic_records"
    id = Column(String, primary_key=True, index=True)
    farmer_id = Column(String, nullable=False, index=True)
    crop_type = Column(String, nullable=False)
    voice_transcript = Column(String, nullable=False)
    language = Column(String, default="Amharic")
    diagnosis = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow, index=True)
