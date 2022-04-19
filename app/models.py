from pydantic import BaseModel, conint, constr

class Produto(BaseModel):
    nome: constr(strip_whitespace=True, to_lower=True)
    link: constr(strip_whitespace=True, to_lower=True)
    quantidade: conint(ge=0)

# model dos parametros das funções:
class Parametros(BaseModel):
    pass

# model para retorno das funções de rota:
class Retorno(BaseModel):
    pass
