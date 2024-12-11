from fastapi import FastAPI
from router import router

app = FastAPI(title="Message Notification Service")
app.include_router(router, tags=["Message Notification"])