from fastapi import FastAPI
from routes.nutrimads import router as router_nutrimads
from routes.alimentos import router as router_alimentos

app = FastAPI()
app.include_router(router_alimentos)
app.include_router(router_nutrimads)
