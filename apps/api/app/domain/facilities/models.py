from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import datetime
from app.db.base import Base

class AgriculturalHub(Base):
    __tablename__ = "agricultural_hubs"

    id = Column(String, primary_key=True, index=True)
    hub_name = Column(String, nullable=False)
    zone = Column(String, nullable=False)
    cooperative_id = Column(String, ForeignKey("farmer_cooperatives.id"), nullable=True, index=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    cooperative = relationship("FarmerCooperative", back_populates="hubs")
    extension_agents = relationship("ExtensionAgent", back_populates="hub", cascade="all, delete-orphan")
