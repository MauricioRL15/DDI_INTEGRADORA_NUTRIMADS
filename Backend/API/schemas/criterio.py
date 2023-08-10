from pydantic import BaseModel
from enum import Enum


class CriterioEstatusEnum(str, Enum):
    Saludable = 'Saludable'
    No_saludable = 'No_saludable'


class Criterio(BaseModel):
    Nombre: str
    Descripcion: str
    Valor_Maximo: float
    Valor_Minimo: float
    Estatus: CriterioEstatusEnum
