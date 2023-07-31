from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from fastapi import Depends

engine = create_engine("mysql+pymysql://root:admin@localhost:3306/bd_nutrimads")

meta = MetaData()

conn = engine.connect()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()