from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from src.shared.base.base_entity import Base
from datetime import datetime, timezone



class SystemLog(Base):
    __tablename__ = "system_logs"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=True)

    event = Column(String(100), nullable=False)

    description = Column(String(255), nullable=False)

    status = Column(String(50), nullable=False)

    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
