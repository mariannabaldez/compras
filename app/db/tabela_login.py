from db.database import *


tabela_login = sqlalchemy.Table(
    "login",
    metadata,
    sqlalchemy.Column(
        "id",
        sqlalchemy.Integer,
        primary_key=True,
        unique=True,
    ),
    sqlalchemy.Column(
        "nome_de_usuario",
        sqlalchemy.String,
        nullable=False,
    ),
    sqlalchemy.Column(
        "senha",
        sqlalchemy.String,
        nullable=False,
    ),
)
