from pydantic import BaseModel
from enum import Enum
from datetime import datetime


class tipo_consumo_enum(str, Enum):
    Consumo_realizado = 'Consumo_realizado'
    Consumo_Sugerido = 'Consumo_Sugerido'


class Consumo(BaseModel):
    ID: int
    Cantidad: float
    Tipo: tipo_consumo_enum
    Estatus: int
    Fecha_Registro: datetime
    Fecha_Actualizacion: datetime
    Usuario_ID: int

class ConsumoInsert(BaseModel):
    Cantidad: float
    Tipo: tipo_consumo_enum
    Usuario_ID: int