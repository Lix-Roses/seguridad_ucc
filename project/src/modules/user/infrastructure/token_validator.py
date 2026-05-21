from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import datetime, timezone
from src.shared.database.connection import get_db
from src.modules.user.infrastructure.token_repository import TokenRepository


def verify_token(data: dict, db: Session = Depends(get_db)):
    token_str = data.get("token")

    if not token_str:
        raise HTTPException(status_code=401, detail="Token no enviado")

    token = TokenRepository.get_by_token(db, token_str)

    if not token:
        raise HTTPException(status_code=401, detail="Token no existe")

    if token.expires_at.replace(tzinfo=timezone.utc) < datetime.now(timezone.utc):
        raise HTTPException(status_code=401, detail="Token expirado")

    return token