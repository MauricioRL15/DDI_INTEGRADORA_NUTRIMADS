from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text 
from config.db import get_db

router = APIRouter()

@router.get("/obtener_datos_vista")
def obtener_datos_vista(db: Session = Depends(get_db)):
    try:
        query = text("SELECT NombreUsuario, NombreAlimento, CantidadComponente FROM vistasencilla;")
        resultados = db.execute(query).fetchall()

        lista_resultados = []
        for resultado in resultados:
            diccionario_resultado = {
                "NombreUsuario": resultado[0],
                "NombreAlimento": resultado[1],
                "CantidadComponente": resultado[2],
            }
            lista_resultados.append(diccionario_resultado)

        return lista_resultados
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# router = APIRouter()

# @router.get("/obtener_datos_vista")
# def obtener_datos_vista(db: Session = Depends(get_db)):
#     query = text("SELECT NombreUsuario, NombreAlimento, CantidadComponente FROM vistasencilla;")
#     result = db.execute(query)
#     data = result.fetchall()
#     return data