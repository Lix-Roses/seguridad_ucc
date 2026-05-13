from passlib.context import CryptContext
import re

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


# Generar hash
def hash_password(password: str):

    return pwd_context.hash(password)


# Verificar contraseña
def verify_password(
    plain_password: str,
    hashed_password: str
):

    return pwd_context.verify(
        plain_password,
        hashed_password
    )


# Validar contraseña segura
def validate_password(password: str):

    # mínimo 8 caracteres
    if len(password) < 8:
        raise ValueError(
            "La contraseña debe tener mínimo 8 caracteres"
        )

    # debe contener número
    if not re.search(r"\d", password):
        raise ValueError(
            "Debe contener un número"
        )

    # debe contener carácter especial
    if not re.search(r"[.@#$%^&+=!]", password):
        raise ValueError(
            "Debe contener un carácter especial"
        )

    return True