from typing import List, Optional
from models.cliente import Cliente
from pydantic import BaseModel


class Pedido(BaseModel):
    id: int
    id_cliente: int
    token: str
    
    class Config:
        from_attributes = True


class StatusPedido(Pedido):
    status: str

class MercadoPago(Pedido):
    codigo: str
    valor_total: float

    class Config:
        from_attributes = True