from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy
import databases

SQLALCHEMY_DATABASE_URL = "sqlite:///./banco_dados.db"

database = databases.Database(SQLALCHEMY_DATABASE_URL)
metadata = sqlalchemy.MetaData()


engine = sqlalchemy.create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

tabela_login = sqlalchemy.Table(
    "login",
    metadata,
    sqlalchemy.Column(
        "id",
        # UUID
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
        sqlalchemy.Integer,
        nullable=False,
    ),
)

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

metadata.create_all(engine)
