from sqlalchemy.orm import Session

from src.modules.user.domain.token_entity import Token


class TokenRepository:

    @staticmethod
    def create(db: Session, token_data: Token):

        db.add(token_data)

        db.commit()

        db.refresh(token_data)

        return token_data

    #Metodo para buscar el token en la base de datos
    @staticmethod
    def get_by_token(db: Session, token: str):
        return db.query(Token).filter(Token.token == token).first()