from fastapi import FastAPI, status

app = FastAPI()


lista_de_compras = {
    "whey": {
            'link': None,
            'quantidade': 0,
    }}

@app.post("/", response_model=dict, status_code=status.HTTP_201_CREATED)
async def adicionar(produto: str, link : str):
    lista_de_compras[produto] = dict()
    lista_de_compras[produto]["link"] = link
    return lista_de_compras

#rota p ver tudo(get), rota pra ver(elemento), rota pra deletar
