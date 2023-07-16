from fastapi import FastAPI
from routes.nutrimads import router

app = FastAPI()
app.include_router(router)
