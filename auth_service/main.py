from fastapi import FastAPI
from routers import router
from model import Base
from session import engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Authorization Service")

app.include_router(router, prefix="/auth", tags=["Auth Service"])