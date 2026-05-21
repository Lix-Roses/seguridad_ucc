from _apple_support import SystemLog

from src.modules.logs.domain.log_entity import SystemLog
from src.modules.logs.infrastructure.log_repository import LogRepository
from src.shared.security.security import (
    hash_password,
    verify_password,
    validate_password
)
from src.modules.user.infrastructure.user_repository import UserRepository
from src.modules.user.infrastructure.token_repository import TokenRepository

from src.modules.user.domain.user_entity import User
from src.modules.user.domain.token_entity import Token

import secrets

from datetime import datetime, timedelta, timezone

class UserService:

    @staticmethod
    def create_user(db, username, email, password):

     validate_password(password)

     hashed_password = hash_password(password)

     user = User(
            username=username,
            email=email,
            password=hashed_password
        )
     return UserRepository.create(db, user)

    @staticmethod
    def get_users(db):
        return UserRepository.get_all(db)

    @staticmethod
    def get_user(db, user_id):
        return UserRepository.get_by_id(db, user_id)

    @staticmethod
    def update_user(db, user_id, data):
        return UserRepository.update(db, user_id, data)

    @staticmethod
    def delete_user(db, user_id):
        return UserRepository.delete(db, user_id)

    @staticmethod
    def login(db, username, password):

        user = UserRepository.get_by_username(db, username)

        if not user:
            return False

        # VERIFICAR HASH
        if not verify_password(password, user.password):
            log = SystemLog(
                event="LOGIN_FAILED",
                description=f"Contraseña incorrecta para: {username}",
                status="FAILED",
                user_id=user.id
            )
            LogRepository.create(db, log)
            return False

        generated_token = secrets.token_hex(32)
        # EXPIRACIÓN 15 MINUTOS
        expires_at = datetime.utcnow() + timedelta(minutes=15)
        token_data = Token(
            token=generated_token,
            user_id=user.id,
            expires_at=expires_at,
        )
        TokenRepository.create(db, token_data)

        log = SystemLog(
            event="LOGIN_SUCCESS",
            description=f"Inicio de sesión exitoso: {username}",
            status="SUCCESS",
            user_id = user.id
        )
        LogRepository.create(db, log)

        colombia_time = expires_at.astimezone()
        return {
            "message": "sesion iniciada",
            "id del usuario": user.id,
            "token": generated_token,
            "expires_at": colombia_time.strftime("%d-%m-%Y %H:%M")
        }