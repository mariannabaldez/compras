from fastapi import FastAPI
from app.routers.produtos import router

app = FastAPI()
app.include_router(router)