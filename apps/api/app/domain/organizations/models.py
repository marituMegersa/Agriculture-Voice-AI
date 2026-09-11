from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship
import datetime
from app.db.base import Base

class FarmerCooperative(Base):
    __tablename__ = "farmer_cooperatives"

    id = Column(String, primary_key=True, index=True)
    coop_name = Column(String, nullable=False)
    region = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    hubs = relationship("AgriculturalHub", back_populates="cooperative", cascade="all, delete-orphan")
