from pydantic import BaseModel
from enum import Enum
from typing import Optional

class FactorEstatusEnum(str, Enum):
    Temprano = 'Temprano'
    Estable = 'Estable'
    Grave = 'Grave'


class Factor(BaseModel):
    Nombre: str
    Estatus: FactorEstatusEnum

class FactorUpdate(BaseModel):
    Nombre: Optional[str]
    Estatus: Optional[FactorEstatusEnum]