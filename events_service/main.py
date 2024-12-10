from fastapi import FastAPI
from routers import router
from model import Base
from session import engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Event Management Service")

app.include_router(router, prefix="/events", tags=["Events"])