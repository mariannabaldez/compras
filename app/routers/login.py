from fastapi import APIRouter, status
from app.models.Login import Login
from app.db.tabela_login import tabela_login, database
import sqlalchemy

router = APIRouter(prefix="/login")

@router.post("/", response_model=dict,)
async def adiciona(login: Login):
    pass


#@router.post("/", response_model=dict, status_code=status.HTTP_201_CREATED)
#async def adiciona(produto: Produto):
#    instrucao = tabela_produtos.insert().values(**produto.dict())
 #   id = await database.execute(instrucao)
 #   return {id: produto}
