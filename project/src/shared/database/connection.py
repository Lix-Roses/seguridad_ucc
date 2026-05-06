from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from shared.config.settings import DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_tables():
    from shared.base.base_entity import Base
    import modules.user.domain.user_entity  # esto registra la tabla
    Base.metadata.create_all(bind=engine)