from fastapi import FastAPI
from routers import router

app = FastAPI() (
    title="API WhatsApp",
    version="1.-.0"
)

app.include_router(router)