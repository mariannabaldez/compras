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
        response = client.post('/produtos/', json=item
        )
    assert response.status_code == 201
    assert response.json()['produto'] == item

def test_criar_novo_produto_str_como_quant_falho():
    item = {
            "nome": "whey",
            "link": "www.google.com.br",
            "quantidade": "string"
    }
    with TestClient(app=app) as client:
        response = client.post('/produtos/', json=item)
    assert response.status_code == 422

def test_criar_novo_produto_quant_negativa_falho():
    item = {
            "nome": "whey",
            "link": "www.google.com.br",
            "quantidade": -2
    }
    with TestClient(app=app) as client:
        response = client.post('/produtos/', json=item)
    assert response.status_code == 422

def test_deletar_novo_produto_sucesso():
    entrada = {
            "nome": "café",
            "link": "https://www.amazon.com.br",
            "quantidade": 1
    }
    saida = {
            "nome": "café",
            "link": "https://www.amazon.com.br",
            "quantidade": 1
        }
    with TestClient(app=app) as client:
        old_response = client.post('/produtos/', json=entrada)
        id = old_response.json()['id']
        response = client.delete(f'/produtos/{id}')
    assert old_response.status_code == 201
    assert old_response.json()['produto'] == saida
    assert response.status_code == 202
    assert response.json() == f"Produto com id: {id} apagado"

def test_deletar_id_nao_encontrado():
    id = 1000
    with TestClient(app=app) as client:
        response = client.delete(f'/produtos/{id}')

    assert response.status_code == 404
    assert response.json()['detail'] == f'produto com id: {id} não existe'

# def test_deletar_novo_produto_falho():
#     with TestClient(app=app) as client:
#         response = client.delete('/produtos/')
#     assert response.status_code == 404

# # teste para confirmar que não da para colocar quantidade de produtos negatva
