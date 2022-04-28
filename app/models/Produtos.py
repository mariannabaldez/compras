from pydantic import AnyUrl, BaseModel, conint, constr


class Produto(BaseModel):
    nome: constr(strip_whitespace=True, to_lower=True) = 'Whey'
    link: AnyUrl = "https://www.google.com.br"
    quantidade: conint(ge=0) = 0