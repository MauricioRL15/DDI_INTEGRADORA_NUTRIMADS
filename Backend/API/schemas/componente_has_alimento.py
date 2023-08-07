from pydantic import BaseModel
from datetime import datetime


class ComponenteHasAlimento(BaseModel):
    componente_ID: int
    alimento_ID: int
    Fecha_Inicio: datetime
    Fecha_Fin: datetime
