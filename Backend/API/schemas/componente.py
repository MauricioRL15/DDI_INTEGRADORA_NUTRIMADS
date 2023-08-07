from pydantic import BaseModel
from enum import Enum


class UnidadMedidaEnum(str, Enum):
    gramo = 'g'
    microgramo = 'µg'
    miligramo = 'mg'
    unidad_internacional = 'UI'
    caloria = 'cal'
    kilocaloria = 'kcal'
    mililitro = 'ml'


class Componente(BaseModel):
    Nombre: str
    Unidad_medida: UnidadMedidaEnum
