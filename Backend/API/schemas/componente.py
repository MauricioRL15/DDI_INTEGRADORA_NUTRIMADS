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
    porcentaje = '%'
    mcg = 'mcg'
    


class Componente(BaseModel):
    Nombre: str
    Cantidad: float
    Unidad_medida: unidad_medida_enum
    Componente_Padre: str
