from fastapi import APIRouter, status
from app.models.Produtos import Produto
from app.db.database import database,tabela_produtos
import sqlalchemy


router = APIRouter(prefix="/produtos")

@router.get("/")
async def visualizar():
    instrucao = tabela_produtos.select()
    return await database.fetch_all(instrucao)
    #database. fetch_all(para retornar tudo) .fetch_one(para retornat um)


@router.get("/{id}")
async def visualizar_elemento(id):
    instrucao = tabela_produtos.select().where(tabela_produtos.c.id==id)
    return await database.execute(instrucao)


@router.post("/", response_model=dict, status_code=status.HTTP_201_CREATED)
async def adiciona(produto: Produto):
    instrucao = tabela_produtos.insert().values(**produto.dict())
    id = await database.execute(instrucao)
    return {id: produto}


@router.delete("/", response_model=str, status_code=status.HTTP_200_OK)
async def deleta(id: int):
    instrucao = tabela_produtos.delete().where(tabela_produtos.c.id==id)
    id = await database.execute(instrucao)
    return f"Produto com id: {id} apagado"


@router.patch("/")
async def altera(id: int, novos_valores: Produto):
    # Acessa produto dentro do "banco de dados" e preenche com novos_valores
    instrucao = tabela_produtos.update().where(tabela_produtos.c.id==id).values(**novos_valores.dict())
    id = await database.execute(instrucao)
    return {id: novos_valores}
