from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import datetime
from app.db.base import Base

class ExtensionAgent(Base):
    __tablename__ = "extension_agents"

    id = Column(String, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    assigned_zone = Column(String, nullable=False)
    hub_id = Column(String, ForeignKey("agricultural_hubs.id"), nullable=True, index=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    hub = relationship("AgriculturalHub", back_populates="extension_agents")
