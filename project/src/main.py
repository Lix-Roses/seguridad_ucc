from fastapi import FastAPI
from src.modules.user.infrastructure.user_controller import router as user_router

from src.shared.database.connection import engine
from src.modules.user.domain.user_entity import Base

from src.modules.logs.domain.log_entity import Base as LogBase
LogBase.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API funcionando"}

app.include_router(user_router)