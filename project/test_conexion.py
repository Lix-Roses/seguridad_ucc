import sys
sys.path.append("src")

from shared.database.connection import engine, create_tables
from sqlalchemy.orm import Session
from modules.user.domain.user_entity import User


create_tables()


with Session(engine) as session:
    usuario = User(
        username="alejandro",
        email="alejandro@test.com",
        password="123456"
    )
    session.add(usuario)
    session.commit()
    print("Usuario creado!")


with Session(engine) as session:
    usuario = session.query(User).filter_by(username="alejandro").first()
    print(f"Usuario encontrado: {usuario.username} - {usuario.email}")