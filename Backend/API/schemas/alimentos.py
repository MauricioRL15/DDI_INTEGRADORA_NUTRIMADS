from pydantic import BaseModel
from enum import Enum
from datetime import datetime

class CantidadEnum(str, Enum):
    Pieza = 'Pieza'
    gramos = 'g'


class GrupoAlimenticioEnum(str, Enum):
    Fruta = 'Fruta'
    Verdura = 'Verdura'
    Cereal = 'Cereal'
    Leguminosa = 'Leguminosa'
    Origen_animal = 'Origen_animal'


class Alimento(BaseModel):
    Nombre: str
    Cantidad: CantidadEnum
    Grupo_alimenticio: GrupoAlimenticioEnum

class AlimentoUpdate(BaseModel):
    Nombre: str
    Cantidad: str
    Grupo_alimenticio: GrupoAlimenticioEnum
    Estatus: int
    Fecha_Actualizacion: datetime

