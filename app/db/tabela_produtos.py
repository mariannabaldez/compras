from app.db.database import *


tabela_produtos = sqlalchemy.Table(
    "produtos",
    metadata,
    sqlalchemy.Column(
        "id",
        sqlalchemy.Integer,
        primary_key=True,
        unique=True,
        ),
    sqlalchemy.Column(
        "nome",
        sqlalchemy.String,
        nullable=False,
    ),
    sqlalchemy.Column(
        "link",
        sqlalchemy.String,
        nullable=True
    ),
    sqlalchemy.Column(
        "quantidade",
        sqlalchemy.Integer,
        nullable=True,
    )
)
