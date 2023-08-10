from pydantic import BaseModel, Field
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

class CriterioCreate(BaseModel):
    Nombre: str
    Descripcion: str
    Valor_Maximo: float
    Valor_Minimo: float
    Estatus: CriterioEstatusEnum

class CriterioUpdate(BaseModel):
    Nombre: str = Field(None, description="Nombre del criterio")
    Descripcion: str = Field(None, description="Descripción del criterio")
    Valor_Maximo: float = Field(None, description="Valor máximo del criterio")
    Valor_Minimo: float = Field(None, description="Valor mínimo del criterio")
    Estatus: CriterioEstatusEnum = Field(None, description="Estatus del criterio")