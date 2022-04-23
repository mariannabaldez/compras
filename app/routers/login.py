from fastapi import APIRouter, status
from app.models.Login import Login
from app.db.tabela_login import tabela_login, database
import sqlalchemy

router = APIRouter(prefix="/login")

@router.get("/")
async def visualizar():
    pass

@router.post("/", response_model=dict,)
async def adiciona(login: Login):
    instrucao = tabela_login.insert().values(**login.dict())
    id = await database.execute(instrucao)
    return {id: login}

@router.delete("/", status_code=status.HTTP_200_OK)
async def deleta(id: int):
    instrucao = tabela_login.delete().where(tabela_login.c.id==id)
    id = await database.execute(instrucao)
    return f"Login com id: {id} apagado"

@router.patch("/")
async def altera(id: int, novos_valores: Login):
    instrucao = tabela_login.update().where(tabela_login.c.id==id).values(**novos_valores.dict())
    id = await database.execute(instrucao)
    return {id: novos_valores}
