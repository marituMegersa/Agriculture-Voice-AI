from sqlalchemy import Column, String, DateTime
import datetime
from app.db.base import Base

class ExtensionAgent(Base):
    __tablename__ = "extension_agents"

    id = Column(String, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    assigned_zone = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
