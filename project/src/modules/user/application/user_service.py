<<<<<<< HEAD
from src.shared.security.security import (
    hash_password,
    verify_password,
    validate_password
)
=======
>>>>>>> a4066e6afaadf778c4bc1fdc8f242eaeaafd8462
from src.modules.user.infrastructure.user_repository import UserRepository
from src.modules.user.domain.user_entity import User


class UserService:

    @staticmethod
    def create_user(db, username, email, password):

<<<<<<< HEAD
     validate_password(password)

     hashed_password = hash_password(password)

     user = User(
            username=username,
            email=email,
            password=hashed_password
        )
     return UserRepository.create(db, user)
=======
        user = User(
            username=username,
            email=email,
            password=password
        )

        return UserRepository.create(db, user)
>>>>>>> a4066e6afaadf778c4bc1fdc8f242eaeaafd8462

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

<<<<<<< HEAD
        if not verify_password(
    password,
    user.password
        ):
         return False
         return True
=======
        if user.password != password:
            return False

        return True
>>>>>>> a4066e6afaadf778c4bc1fdc8f242eaeaafd8462
