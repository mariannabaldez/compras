from pydantic import BaseModel, conint, constr


class Produto(BaseModel):
    nome: constr(strip_whitespace=True, to_lower=True)
    link: constr(strip_whitespace=True, to_lower=True)
    quantidade: conint(ge=0)
