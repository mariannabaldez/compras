from urllib import response
import pytest
from httpx import AsyncClient

from .main import app

@pytest.mark.anyio
async def test_visualizar_produto_passando_id_valido():
    async whith AsyncClient(app=app, base_url="http://127.0.0.1:8000") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"mensagem": }


@pytest.mark.anyio
async def test_visualizar_produto_passando_id_invalido():
    async whith AsyncClient(app=app, base_url="http://127.0.0.1:8000") as ac:
        response = await ac.get("/")
    assert response.status_code == 400
    assert response.json() == {"mensagem": "id invalido"}


# teste para confirmar que não da para colocar quantidade de produtos negatva

# exemplo:
@pytest.mark.anyio
async def test_root():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Tomato"}