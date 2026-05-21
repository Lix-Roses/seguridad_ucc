from sqlalchemy import Column, DateTime, Boolean
from datetime import datetime


class AuditableEntity:
    created_at = Column(DateTime, default=datetime.utcnow)

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    deleted_at = Column(DateTime, nullable=True)

    state = Column(Boolean, default=True)