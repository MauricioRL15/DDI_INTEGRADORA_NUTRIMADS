from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from schemas.criterio import Criterio, CriterioCreate, CriterioUpdate
from config.db import get_db
from models.nutrimads import criterio 
from sqlalchemy import update

router = APIRouter()

@router.get("/getAllCriterios")
def obtener_criterios(db: Session = Depends(get_db)):
    try:
        lista_tupla_criterios = db.execute(criterio.select()).fetchall()
        lista_diccionario_criterios = []
        for tupla_criterio in lista_tupla_criterios:
            diccionario_criterio = {
                "ID": tupla_criterio[0],
                "Nombre": tupla_criterio[1],
                "Descripcion": tupla_criterio[2],
                "Valor_Maximo": tupla_criterio[3],
                "Valor_Minimo": tupla_criterio[4],
                "Estatus": tupla_criterio[5],
                "Fecha_Registro": tupla_criterio[6],
                "Fecha_Actualizacion": tupla_criterio[7]
            }
            lista_diccionario_criterios.append(diccionario_criterio)
        return lista_diccionario_criterios
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/getCriterio/{criterio_id}")
def obtener_criterio(criterio_id: int, db: Session = Depends(get_db)):
    try:
        tupla_criterio = db.execute(criterio.select().where(criterio.c.ID == criterio_id)).first()
        if tupla_criterio:
            diccionario_criterio = {
                "ID": tupla_criterio[0],
                "Nombre": tupla_criterio[1],
                "Descripcion": tupla_criterio[2],
                "Valor_Maximo": tupla_criterio[3],
                "Valor_Minimo": tupla_criterio[4],
                "Estatus": tupla_criterio[5],
                "Fecha_Registro": tupla_criterio[6],
                "Fecha_Actualizacion": tupla_criterio[7]
            }
            return diccionario_criterio
        else:
            return {"status": "No existe ese criterio"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/insertCriterio")
def insertar_criterio(criterio_data: CriterioCreate, db: Session = Depends(get_db)):
    try:
        nuevo_criterio = criterio.insert().values(**criterio_data.dict())
        db.execute(nuevo_criterio)
        db.commit()
        return {"status": "Criterio insertado con éxito"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.put("/updateCriterio/{criterio_id}")
def actualizar_criterio(criterio_id: int, criterio_data: CriterioUpdate, db: Session = Depends(get_db)):
    # Verificar si el ID del criterio existe en la base de datos
    criterio_existente = db.execute(criterio.select().where(criterio.c.ID == criterio_id)).fetchone()
    if criterio_existente is None:
        raise HTTPException(status_code=404, detail="Criterio no encontrado")
    
    criterio_actualizado = {
        "Nombre": criterio_data.Nombre,
        "Descripcion": criterio_data.Descripcion,
        "Valor_Maximo": criterio_data.Valor_Maximo,
        "Valor_Minimo": criterio_data.Valor_Minimo,
        "Estatus": criterio_data.Estatus,
    }
    
    stmt = update(criterio).where(criterio.c.ID == criterio_id).values(**criterio_actualizado)
    db.execute(stmt)
    db.commit()
    
    return {"status": "Criterio actualizado con éxito"}

@router.delete("/deleteCriterio/{criterio_id}")
def eliminar_criterio(criterio_id: int, db: Session = Depends(get_db)):
    try:
        stmt = criterio.delete().where(criterio.c.ID == criterio_id)
        db.execute(stmt)
        db.commit()
        return {"status": "Criterio eliminado con éxito"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))