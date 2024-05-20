from typing import Optional
from pydantic import BaseModel


class Cliente(BaseModel):
    id: Optional[int] = None
    cpf: str
    nome: Optional[str] = None
    email: Optional[str] = None
    dtcriacao: str
    class Config:
        from_attributes = True