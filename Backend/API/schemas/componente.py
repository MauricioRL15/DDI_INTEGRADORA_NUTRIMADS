from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional


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

class ComponenteCreate(BaseModel):
    Nombre: str
    Cantidad: float
    Unidad_medida: unidad_medida_enum
    Estatus: bool = True
    Componente_Padre: Optional[str] = None

class ComponenteUpdate(BaseModel):
    Nombre: str
    Cantidad: float
    Unidad_medida: unidad_medida_enum
    Estatus: int = Field(..., ge=0, le=1)