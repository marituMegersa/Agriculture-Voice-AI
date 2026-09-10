from sqlalchemy import Column, String, DateTime
import datetime
from app.db.base import Base

class AgriculturalHub(Base):
    __tablename__ = "agricultural_hubs"

    id = Column(String, primary_key=True, index=True)
    hub_name = Column(String, nullable=False)
    zone = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
