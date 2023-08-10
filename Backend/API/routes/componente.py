from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.componente import Componente, ComponenteCreate, ComponenteUpdate
from config.db import get_db
from models.nutrimads import componente
from sqlalchemy import update


router = APIRouter()

@router.get("/getAllComponentes")
def obtener_componentes(db: Session = Depends(get_db)):
    try:
        lista_tupla_componentes = db.execute(componente.select()).fetchall()
        lista_diccionario_componentes = []
        for tupla_componente in lista_tupla_componentes:
            diccionario_componente = {
                "ID": tupla_componente[0],
                "Nombre": tupla_componente[1],
                "Cantidad":tupla_componente[2],
                "Unidad_medida": tupla_componente[3],
                "Estatus": int.from_bytes(tupla_componente[4], byteorder='big'),
                "Fecha_Registro": tupla_componente[5],  
                "Fecha_Actualizacion": tupla_componente[6],  
                "Componente_Padre":tupla_componente[7]
            }
            lista_diccionario_componentes.append(diccionario_componente)
        return lista_diccionario_componentes
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/insertComponente")
def insertar_componente(componente_data: ComponenteCreate, db: Session = Depends(get_db)):
    try:
        nuevo_componente = componente.insert().values(**componente_data.dict())
        db.execute(nuevo_componente)
        db.commit()
        return {"status": "Componente insertado con éxito"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/getComponente/{componente_id}")
def obtener_componente(componente_id: int, db: Session = Depends(get_db)):
    try:
        tupla_componente = db.execute(componente.select().where(componente.c.ID == componente_id)).first()
        if tupla_componente:
            diccionario_componente = {
                "ID": tupla_componente[0],
                "Nombre": tupla_componente[1],
                "Cantidad": tupla_componente[2],
                "Unidad_medida": tupla_componente[3],
                "Estatus": int.from_bytes(tupla_componente[4], byteorder='big'),
                "Fecha_Registro": tupla_componente[5],
                "Fecha_Actualizacion": tupla_componente[6],
                "Componente_Padre": tupla_componente[7]
            }
            return diccionario_componente
        else:
            return {"status": "No existe ese componente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.put("/updateComponente/{componente_id}")
def actualizar_componente(componente_id: int, componente_data: ComponenteUpdate, db: Session = Depends(get_db)):
    # Verificar si el ID del componente existe en la base de datos
    componente_existente = db.execute(componente.select().where(componente.c.ID == componente_id)).fetchone()
    if componente_existente is None:
        raise HTTPException(status_code=404, detail="Componente no encontrado")
    
    componente_actualizado = {
        "Nombre": componente_data.Nombre,
        "Cantidad": componente_data.Cantidad,
        "Unidad_medida": componente_data.Unidad_medida,
        "Estatus": componente_data.Estatus,
    }
    
    stmt = update(componente).where(componente.c.ID == componente_id).values(**componente_actualizado)
    db.execute(stmt)
    db.commit()
    
    return {"status": "Componente actualizado con éxito"}

@router.delete("/deleteComponente/{componente_id}")
def eliminar_componente(componente_id: int, db: Session = Depends(get_db)):
    try:
        stmt = componente.delete().where(componente.c.ID == componente_id)
        db.execute(stmt)
        db.commit()
        return {"status": "Componente eliminado con éxito"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
