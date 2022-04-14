from fastapi import FastAPI, status
from pydantic import BaseModel
app = FastAPI()

class Produto(BaseModel):
    link: str
    quantidade: int

lista_de_compras = {
    "whey": {
            'link': None,
            'quantidade': 0,
    },
    "ovo": {
        'link': None,
        'quantidade': 0,
    }
}


@app.get("/")
async def visualizar():
    return lista_de_compras

@app.get("/{item}")
async def visualizar_elemento(item):
    return lista_de_compras[item]

@app.post("/", response_model=dict, status_code=status.HTTP_201_CREATED)
async def adiciona(produto: str, link: str):
    lista_de_compras[produto] = dict()
    lista_de_compras[produto]["link"] = link
    return lista_de_compras

@app.delete("/")
async def deleta(produto: str):
    return lista_de_compras.pop(produto, False)

@app.patch("/")
async def altera(novos_valores: Produto, produto: str):
    # Acessa produto dentro do "banco de dados" e preenche com novos_valores
    lista_de_compras[produto] = {**novos_valores.dict()} # a var produto - não é a key e sim o value que estaa associado a key

    return lista_de_compras
#rota p ver tudo(get) ok, rota pra ver(elemento) ok, rota pra deletar
