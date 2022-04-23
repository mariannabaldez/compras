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

metadata.create_all(engine)
