from pydantic import BaseModel
from datetime import datetime, date
from enum import Enum
from typing import Optional


class GeneroEnum(str, Enum):
    Femenino = 'Femenino'
    Masculino = 'Masculino'
    No_Binario = 'No_Binario'

class EstatusEnum(str, Enum):
    Activo = 'Activo'
    Inactivo = 'Inactivo'

class Usuario(BaseModel):
    Nombre: str
    Genero: GeneroEnum
    Peso: float
    Talla: float
    Fecha_Nacimiento: date
    Estatus: EstatusEnum

