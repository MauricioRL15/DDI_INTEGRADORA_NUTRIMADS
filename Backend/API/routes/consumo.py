from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from schemas.consumo import Consumo, ConsumoInsert
from config.db import get_db
from models.nutrimads import consumo 

router = APIRouter()

@router.get("/getAllConsumos")
def obtener_consumos(db: Session = Depends(get_db)):
    try:
        lista_tupla_consumos = db.execute(consumo.select()).fetchall()
        lista_diccionario_consumos = []
        for tupla_consumo in lista_tupla_consumos:
            diccionario_consumo = {
                "ID": tupla_consumo[0],
                "Cantidad": tupla_consumo[1],
                "Tipo": tupla_consumo[2],
                "Estatus": int.from_bytes(tupla_consumo[3], byteorder='big'),
                "Fecha_Registro": tupla_consumo[4],
                "Fecha_Actualizacion": tupla_consumo[5],
                "Usuario_ID": tupla_consumo[6]
            }
            lista_diccionario_consumos.append(diccionario_consumo)
        return lista_diccionario_consumos
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/insertConsumo")
def insertar_consumo(consumo_data: ConsumoInsert, db: Session = Depends(get_db)):
    try:
        nuevo_consumo = consumo.insert().values(**consumo_data.dict())
        db.execute(nuevo_consumo)
        db.commit()
        return {"status": "Consumo insertado con éxito"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
