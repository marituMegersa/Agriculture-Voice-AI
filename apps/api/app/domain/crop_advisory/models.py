from sqlalchemy import Column, String, Boolean, DateTime, Float, Integer, JSON
import datetime
from app.db.base import Base

class CropAdvisoryRecord(Base):
    __tablename__ = "crop_advisory_records"

    id = Column(String, primary_key=True, index=True)

    farmer_id = Column(String, nullable=False, index=True)
    crop_type = Column(String, nullable=False)
    language = Column(String, default="am") # amharic / afaan_oromo
    voice_audio_url = Column(String, nullable=True)
    diagnostic_result = Column(String, nullable=False)
    recommended_treatment = Column(String, nullable=False)

    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
