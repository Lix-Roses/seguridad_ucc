from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from src.shared.base.base_entity import Base
from src.shared.base.auditable_entity import AuditableEntity


class SystemLog(Base, AuditableEntity):
    __tablename__ = "system_logs"

    id = Column(Integer, primary_key=True, index=True)

    event = Column(String(100), nullable=False)

    description = Column(String(255), nullable=False)

    status = Column(String(50), nullable=False)

    created_by = Column(String(100), nullable=True)

    ip_address = Column(String(50), nullable=True)

    created_log_at = Column(DateTime, default=datetime.utcnow)