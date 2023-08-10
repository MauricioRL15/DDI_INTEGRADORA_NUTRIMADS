from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from typing import List

from schemas.alimentos import Alimento, AlimentoUpdate
from config.db import get_db, engine, conn
from models.nutrimads import alimento as alimento_model
from sqlalchemy import select
from models.nutrimads import alimento
from sqlalchemy import update

router = APIRouter()



@router.get("/getAllAlimentos")
def obtenerTodosLosAlimentos():
    try:
        lista_tupla_alimentos = conn.execute(alimento_model.select().limit(100)).fetchall()
        lista_alimentos = [
            {
                "ID": tupla_alimento[0],
                "Nombre": tupla_alimento[1],
                "Cantidad": tupla_alimento[2],
                "Grupo_alimenticio": tupla_alimento[3],
                "Estatus": int.from_bytes(tupla_alimento[4], byteorder='big'),
                "Fecha_Registro": tupla_alimento[5],
                "Fecha_Actualizacion": tupla_alimento[6],
            }
            for tupla_alimento in lista_tupla_alimentos
        ]
        return lista_alimentos
    except Exception as e:
        return {"error": str(e)}
    
@router.post("/insertAlimento")
def insertarAlimento(alimento_data: Alimento, db: Session = Depends(get_db)):
    try:
        alimento_dict = dict(alimento_data)
        conn.execute(alimento_model.insert().values(alimento_dict))
        conn.commit()
        return {"status": "Alimento insertado con éxito"}
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))

# @router.get("/getAlimentoPorNombre2/{nombre_alimento}", response_model=Alimento)
# def obtener_alimento_por_nombre(nombre_alimento: str, db: Session = Depends(get_db)):
#     alimento = db.query(alimento_model).filter(alimento_model.c.Nombre == nombre_alimento).first()
#     if alimento is None:
#         raise HTTPException(status_code=404, detail="Alimento no encontrado")
#     return alimento

@router.get("/getAlimentoPorNombre")
def obtenerAlimentoPorNombre(nombre: str):
    tupla_alimento = conn.execute(
        alimento.select().where(alimento.c.Nombre == nombre)
    ).first()
    if tupla_alimento:
        diccionario_alimento = {
            "ID": tupla_alimento[0],
            "Nombre": tupla_alimento[1],
            "Cantidad": tupla_alimento[2],
            "Grupo_alimenticio": tupla_alimento[3],
            "Estatus": int.from_bytes(tupla_alimento[4], byteorder='big'),
            "Fecha_Registro": tupla_alimento[5].strftime("%Y-%m-%d %H:%M:%S"),
            "Fecha_Actualizacion": tupla_alimento[6].strftime("%Y-%m-%d %H:%M:%S")
            if tupla_alimento[6]
            else None,
        }
        return diccionario_alimento
    else:
        res = {"status": "No existe ese alimento"}
        return res


@router.get("/getOneAlimento/{id_alimento}")
def obtenerAlimento(id_alimento):
    tupla_alimento = conn.execute(
        alimento.select().where(alimento.c.ID == id_alimento)
    ).first()
    if tupla_alimento:
        diccionario_alimento = {
            "ID": tupla_alimento[0],
            "Nombre": tupla_alimento[1],
            "Cantidad": tupla_alimento[2],
            "Grupo_alimenticio": tupla_alimento[3],
            "Estatus": int.from_bytes(tupla_alimento[4], byteorder='big'),
            "Fecha_Registro": tupla_alimento[5].strftime("%Y-%m-%d %H:%M:%S"),
            "Fecha_Actualizacion": tupla_alimento[6].strftime("%Y-%m-%d %H:%M:%S")
            if tupla_alimento[6]
            else None,
        }
        return diccionario_alimento
    else:
        res = {"status": "No existe ese alimento"}
        return res

@router.put("/updateAlimento/{alimento_id}")
def actualizar_alimento(alimento_id: int, alimento_data: AlimentoUpdate, db: Session = Depends(get_db)):
    alimento_actualizado = {
        "Nombre": alimento_data.Nombre,
        "Cantidad": alimento_data.Cantidad,
        "Grupo_alimenticio": alimento_data.Grupo_alimenticio,
    }
    
    stmt = update(alimento_model).where(alimento_model.c.ID == alimento_id).values(**alimento_actualizado)
    db.execute(stmt)
    db.commit()
    
    return {"status": "Alimento actualizado con éxito"}


