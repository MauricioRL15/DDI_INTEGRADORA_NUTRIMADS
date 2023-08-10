from pydantic import BaseModel
from enum import Enum


class unidad_medida_enum(str, Enum):
    gramo = 'g'
    microgramo = 'µg'
    miligramo = 'mg'
    unidad_internacional = 'UI'
    caloria = 'cal'
    kilocaloria = 'kcal'
    mililitro = 'ml'


class Componente(BaseModel):
    Nombre: str
    Unidad_medida: unidad_medida_enum
