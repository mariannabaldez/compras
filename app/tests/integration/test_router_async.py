import pytest
from starlette.testclient import TestClient

from app import main
app = main.app


def test_criar_novo_produto_sucesso():
    item = {
            "nome": "whey",
            "link": "https://www.google.com.br",
            "quantidade": 3
    }
    with TestClient(app=app) as client:
        response = client.post(
            '/produtos/',
            json= item
        )

    assert response.status_code == 201
    assert response.json() == {'produto cadastrado': item}


def test_criar_novo_produto_falho():
    item = {
            "nome": "whey",
            "link": "www.google.com.br",
            "quantidade": 3
    }
    with TestClient(app=app) as client:
        response = client.post('/produtos/', json=item)
    assert response.status_code == 422

def test_deletar_novo_produto_sucesso():
    item = {
            "nome": "whey",
            "link": "www.google.com.br",
            "quantidade": 3
    }
    with TestClient(app=app) as client:
        response = client.delete('/produtos/', json=item)
    assert response.status_code == 200

# teste para confirmar que não da para colocar quantidade de produtos negatva
