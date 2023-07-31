from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List

from schemas.alimentos import Alimento
from config.db import get_db, engine, conn
from models.nutrimads import alimento as alimento_model
from sqlalchemy import select
from models.nutrimads import alimento

router = APIRouter()

'''
Con limite
@router.get("/getAllAlimentos", response_model=List[Alimento])
def obtener_alimentos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    query = select(alimento).offset(skip).limit(limit)
    alimentos = db.execute(query).fetchall()
    return alimentos
'''


@router.get("/getAllAlimentos")
def obtenerTodosLosAlimentos(skip: int = Query(0, ge=0)):
    lista_tupla_alimentos = conn.execute(
        alimento_model.select().offset(skip).limit(100)
    ).fetchall()
    lista_alimentos = [
        {
            "ID": tupla_alimento[0],
            "Nombre": tupla_alimento[1],
            "Cantidad": tupla_alimento[2],
            "Grupo_alimenticio": tupla_alimento[3],
            "Estatus": "Inactivo" if tupla_alimento[4] == 1 else "Activo",
            "Fecha_Registro": tupla_alimento[5].strftime("%Y-%m-%d %H:%M:%S"),
            "Fecha_Actualizacion": tupla_alimento[6].strftime("%Y-%m-%d %H:%M:%S") if tupla_alimento[6] else None,
        }
        for tupla_alimento in lista_tupla_alimentos
    ]
    return lista_alimentos