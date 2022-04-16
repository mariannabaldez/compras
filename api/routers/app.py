from fastapi import APIRouter, status
from models.schemas.produto import Produto
from db.lista_de_compras import lista_de_compras

router = APIRouter(tags=['Produtos'])


@router.get("/")
async def visualizar():
    return lista_de_compras

@router.get("/{item}")
async def visualizar_elemento(item):
    return lista_de_compras[item]

@router.post("/", response_model=dict, status_code=status.HTTP_201_CREATED)
async def adiciona(produto: str, link: str):
    lista_de_compras[produto] = dict()
    lista_de_compras[produto]["link"] = link
    return lista_de_compras

@router.delete("/")
async def deleta(produto: str):
    return lista_de_compras.pop(produto, False)

@router.patch("/")
async def altera(novos_valores: Produto, produto: str):
    # Acessa produto dentro do "banco de dados" e preenche com novos_valores
    lista_de_compras[produto] = {**novos_valores.dict()} # a var produto - não é a key e sim o value que estaa associado a key
    return lista_de_compras