from fastapi import FastAPI
from fastapi.routing import APIRouter
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str
    app_env: str
    app_port: int
    secret_key: str

    class Config:
        env_file = ".env"

settings = Settings()

app = FastAPI(title=settings.app_name)

router = APIRouter(prefix="/api")

@app.get("/")
def root():
    return {"message": "Welcome", "app": settings.app_name}

@app.get("/health")
def health():
    return {"status": "ok"}

@router.get("/info")
def info():
    return {
        "app_name": settings.app_name,
        "environment": settings.app_env,
        "port": settings.app_port
    }

app.include_router(router)