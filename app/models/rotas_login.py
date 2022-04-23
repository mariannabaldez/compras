from pydantic import BaseModel, conint, constr


# model dos parametros das funções:
class Parametros(BaseModel):
    pass

# model para retorno das funções de rota:
class Retorno(BaseModel):
    pass