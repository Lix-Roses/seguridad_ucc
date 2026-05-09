from fastapi import FastAPI
from src.modules.user.infrastructure.user_controller import router as user_router

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API funcionando"}

app.include_router(user_router)