from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from src.shared.base.base_entity import Base


class Token(Base):
    __tablename__ = "tokens"

    id = Column(Integer, primary_key=True, index=True)

    token = Column(String(255), nullable=False)

    user_id = Column(Integer, ForeignKey("users.id"))

    expires_at = Column(DateTime, nullable=False)