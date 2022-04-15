from fastapi import FastAPI
from models.schemas.produto import Produto
from db.lista_de_compras import lista_de_compras

from api.routers.app import *