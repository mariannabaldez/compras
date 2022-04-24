from fastapi import APIRouter
from app.routers import login, produtos

router = APIRouter()
router.include_router(login.router, tags=["login"], prefix="/users")
router.include_router(produtos.router, tags=["produtos"], prefix="/produtos")