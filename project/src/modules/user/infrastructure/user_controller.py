from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.shared.database.connection import get_db
from src.modules.user.application.user_service import UserService

router = APIRouter()


# CREAR USUARIO
@router.post("/users")
def create_user(data: dict, db: Session = Depends(get_db)):

    user = UserService.create_user(
        db,
        data["username"],
        data["email"],
        data["password"]
    )

    return {
        "message": "usuario creado",
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email
        }
    }


# LISTAR USUARIOS
@router.get("/users")
def get_users(db: Session = Depends(get_db)):

    return UserService.get_users(db)


# OBTENER USUARIO
@router.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):

    user = UserService.get_user(db, user_id)

    if not user:
        raise HTTPException(status_code=404, detail="usuario no encontrado")

    return user


# ACTUALIZAR USUARIO
@router.put("/users/{user_id}")
def update_user(user_id: int, data: dict, db: Session = Depends(get_db)):

    user = UserService.update_user(db, user_id, data)

    if not user:
        raise HTTPException(status_code=404, detail="usuario no encontrado")

    return {
        "message": "usuario actualizado"
    }


# ELIMINAR USUARIO
@router.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):

    user = UserService.delete_user(db, user_id)

    if not user:
        raise HTTPException(status_code=404, detail="usuario no encontrado")

    return {
        "message": "usuario eliminado"
    }


# LOGIN
@router.post("/login")
def login(data: dict, db: Session = Depends(get_db)):

    success = UserService.login(
        db,
        data["username"],
        data["password"]
    )

    if not success:
        raise HTTPException(
            status_code=204,
            detail="credenciales incorrectas"
        )

    return {
        "message": "sesion iniciada"
    }