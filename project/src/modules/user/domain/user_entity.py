from sqlalchemy import Column, Integer, String
from src.shared.base.base_entity import Base
from src.shared.base.auditable_entity import AuditableEntity

class User(Base, AuditableEntity):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)