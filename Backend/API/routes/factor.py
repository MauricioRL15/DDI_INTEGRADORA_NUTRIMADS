from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from schemas.factor import Factor, FactorUpdate
from config.db import get_db
from models.nutrimads import factor
from sqlalchemy import update

router = APIRouter()

@router.get("/getAllFactores")
def obtener_factores(db: Session = Depends(get_db)):
    try:
        lista_tupla_factores = db.execute(factor.select()).fetchall()
        lista_diccionario_factores = []
        for tupla_factor in lista_tupla_factores:
            diccionario_factor = {
                "ID": tupla_factor[0],
                "Nombre": tupla_factor[1],
                "Estatus": tupla_factor[2],
                "Fecha_Registro": tupla_factor[3],
                "Fecha_Actualizacion": tupla_factor[4],
            }
            lista_diccionario_factores.append(diccionario_factor)
        return lista_diccionario_factores
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/getFactor/{factor_id}")
def obtener_factor(factor_id: int, db: Session = Depends(get_db)):
    try:
        tupla_factor = db.execute(factor.select().where(factor.c.ID == factor_id)).first()
        if tupla_factor:
            diccionario_factor = {
                "ID": tupla_factor[0],
                "Nombre": tupla_factor[1],
                "Estatus": tupla_factor[2],
                "Fecha_Registro": tupla_factor[3],
                "Fecha_Actualizacion": tupla_factor[4],
            }
            return diccionario_factor
        else:
            return {"status": "No existe ese factor"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/insertFactor")
def insertar_factor(factor_data: Factor, db: Session = Depends(get_db)):
    try:
        nuevo_factor = factor.insert().values(**factor_data.dict())
        db.execute(nuevo_factor)
        db.commit()
        return {"status": "Factor insertado con éxito"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/updateFactor/{factor_id}")
def actualizar_factor(factor_id: int, factor_data: FactorUpdate, db: Session = Depends(get_db)):
    factor_existente = db.execute(factor.select().where(factor.c.ID == factor_id)).fetchone()
    if factor_existente is None:
        raise HTTPException(status_code=404, detail="Factor no encontrado")
    
    factor_actualizado = {
        "Nombre": factor_data.Nombre,
        "Estatus": factor_data.Estatus,
    }
    
    stmt = update(factor).where(factor.c.ID == factor_id).values(**factor_actualizado)
    db.execute(stmt)
    db.commit()
    
    return {"status": "Factor actualizado con éxito"}

@router.delete("/deleteFactor/{factor_id}")
def eliminar_factor(factor_id: int, db: Session = Depends(get_db)):
    try:
        stmt = factor.delete().where(factor.c.ID == factor_id)
        result = db.execute(stmt)
        db.commit()
        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail="Factor no encontrado")
        return {"status": "Factor eliminado con éxito"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
