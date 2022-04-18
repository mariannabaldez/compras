from fastapi import APIRouter, status
from app.models import Produto
from app.database import tabela_produtos, database
lista_de_compras = {}
router = APIRouter(prefix="/produtos")

@router.get("/")
async def visualizar():
    return lista_de_compras


@router.get("/{item}")
async def visualizar_elemento(item):
    return lista_de_compras[item]


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
