from urllib import response
import pytest
from httpx import AsyncClient
from app.db.database import database,tabela_produtos

from app import main
app = main.app

item = {1}

@pytest.mark.anyio
async def test_visualizar_produto_passando_id_valido():
    async with AsyncClient(app=app, base_url="//127.0.0.1:8000/produtos/produtos/item") as ac:
        response = await ac.get("/produtos")
    assert response.status_code == 200
    assert database.execute(tabela_produtos.select().where(tabela_produtos.c.id==id))


# teste para confirmar que não da para colocar quantidade de produtos negatva
