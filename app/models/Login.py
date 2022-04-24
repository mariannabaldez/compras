from pydantic import BaseModel, conint, constr


class Login(BaseModel):
    nome_de_usuario: constr(strip_whitespace=True, to_lower=True)
    senha: constr(min_length=4)
