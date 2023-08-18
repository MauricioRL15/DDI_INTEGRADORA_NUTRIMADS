from fastapi import FastAPI
from routes.nutrimads import router as router_nutrimads
from routes.alimentos import router as router_alimentos
from routes.componente import router as router_componete
from routes.consumo import router as router_consumo
from routes.criterio import router as router_criterio
from routes.factor import router as router_factor
from routes.vista import router as router_vista


app = FastAPI()

app.include_router(router_alimentos, prefix="/alimentos", tags=["Alimentos"])
app.include_router(router_componete, prefix="/componentes", tags=["Componentes"])
app.include_router(router_nutrimads, prefix="/usuarios", tags=["Usuarios"])
app.include_router(router_consumo, prefix="/consumo", tags=["Consumo"])
app.include_router(router_criterio, prefix="/criterio", tags=["Criterio"])
app.include_router(router_factor, prefix="/factor", tags=["Factor"])
app.include_router(router_vista, prefix="/vista", tags=["Vista"])

# app.include_router()
# app.include_router()
# app.include_router()
