from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.shared.database.connection import get_db
from src.modules.user.application.user_service import UserService
from src.modules.user.infrastructure.token_validator import verify_token
from sqlalchemy.exc import IntegrityError

router = APIRouter()


# CREAR USUARIO
@router.post("/users")
def create_user(data: dict, db: Session = Depends(get_db)):

    try:
        user = UserService.create_user(
            db,
            data["username"],
            data["email"],
            data["password"]
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except IntegrityError as e:
        db.rollback()
        if "username" in str(e.orig):
            raise HTTPException(status_code=400, detail="El usuario ya existe")
        if "email" in str(e.orig):
            raise HTTPException(status_code=400, detail="El correo ya está registrado")
        raise HTTPException(status_code=400, detail="Datos duplicados")

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
def update_user(user_id: int, data: dict, db: Session = Depends(get_db), token=Depends(verify_token)):
    if token.user_id != user_id:
        raise HTTPException(status_code=403, detail="No tienes permiso para modificar este usuario")

    user = UserService.update_user(db, user_id, data)
    if not user:
        raise HTTPException(status_code=404, detail="usuario no encontrado")
    return {"message": "usuario actualizado"}

# ELIMINAR USUARIO
@router.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db), token=Depends(verify_token)):
    if token.user_id != user_id:
        raise HTTPException(status_code=403, detail="No tienes permiso para eliminar este usuario")

    user = UserService.delete_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="usuario no encontrado")
    return {"message": "usuario eliminado"}


# LOGIN
@router.post("/login")
def login(data: dict, db: Session = Depends(get_db)):

    response = UserService.login(
        db,
        data["username"],
        data["password"]
    )

    if not response:
        raise HTTPException(
            status_code=401,
            detail="Usuario o contraseña incorrectos"
        )

    return response