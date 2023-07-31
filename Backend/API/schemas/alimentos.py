from pydantic import BaseModel
from enum import Enum


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
