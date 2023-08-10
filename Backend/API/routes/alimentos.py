from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List

from schemas.alimentos import Alimento
from config.db import get_db, engine, conn
from models.nutrimads import alimento as alimento_model
from sqlalchemy import select
from models.nutrimads import alimento

router = APIRouter()



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
            # "Valor_Calorico" : tupla_alimento[3],
            "Grupo_alimenticio": tupla_alimento[3],
            "Estatus": int.from_bytes(tupla_alimento[4], byteorder='big'),
            "Fecha_Registro": tupla_alimento[5],
            "Fecha_Actualizacion": tupla_alimento[6],
        }
        for tupla_alimento in lista_tupla_alimentos
    ]
    return lista_alimentos