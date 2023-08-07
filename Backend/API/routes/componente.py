from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from config.db import engine, get_db
from models.nutrimads import ComponenteHasAlimento, componente, alimento
from schemas.alimentos import Alimento
from schemas.componente import Componente

router_alimentos = APIRouter()

@router_alimentos.get("/calorias/{alimento_nombre}")
def calcular_calorias(alimento_nombre: str, db: Session = Depends(get_db)):
    # Obtener el ID del alimento
    stmt = select(alimento.c.ID).where(alimento.c.Nombre == alimento_nombre)
    result = db.execute(stmt).fetchone()
    if result is None:
        raise HTTPException(status_code=404, detail="Alimento no encontrado")

    alimento_id = result[0]

    # Obtener los componentes del alimento
    stmt = select(ComponenteHasAlimento.c.componente_ID).where(ComponenteHasAlimento.c.alimento_ID == alimento_id)
    componentes_ids = [row[0] for row in db.execute(stmt).fetchall()]

    # Obtener los valores nutricionales de los componentes y calcular las calorías
    total_calorias = 0
    for componente_id in componentes_ids:
        stmt = select(componente).where(componente.c.ID == componente_id)
        componente_info = db.execute(stmt).fetchone()
        if componente_info:
            total_calorias += componente_info.Valor_calorico

    return {"alimento": alimento_nombre, "calorias": total_calorias} 
