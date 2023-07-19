from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:1234@localhost:3307/bd_nutrimads")

meta = MetaData()

conn = engine.connect()
