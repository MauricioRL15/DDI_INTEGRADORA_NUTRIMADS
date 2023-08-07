from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.componente import Componente  
from config.db import get_db
from models.nutrimads import componente

router = APIRouter()

@router.get("/getAllComponentes")
def obtener_componentes(db: Session = Depends(get_db)):
    lista_tupla_componentes = db.execute(componente.select()).fetchall()
    lista_diccionario_componentes = []
    for tupla_componente in lista_tupla_componentes:
        diccionario_componente = {
            "ID": tupla_componente[0],
            "Nombre": tupla_componente[1],
            "Componente_Padre":tupla_componente[2],
            "Unidad_medida": tupla_componente[3],
            "Estatus": int.from_bytes(tupla_componente[4], byteorder='big'),
            "Fecha_Registro": tupla_componente[5],  
            "Fecha_Actualizacion": tupla_componente[6]  
        }
        lista_diccionario_componentes.append(diccionario_componente)
    return lista_diccionario_componentes