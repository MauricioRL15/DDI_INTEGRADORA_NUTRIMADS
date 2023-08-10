from pydantic import BaseModel
from enum import Enum


class FactorEstatusEnum(str, Enum):
    Temprano = 'Temprano'
    Estable = 'Estable'
    Grave = 'Grave'


class Factor(BaseModel):
    Nombre: str
    Estatus: FactorEstatusEnum
