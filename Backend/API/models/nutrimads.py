from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Enum, Float, Date, DateTime
from sqlalchemy.dialects.mysql import ENUM
from config.db import meta, engine
import datetime


genero_enum = ENUM("Femenino", "Masculino", "No_Binario", name="genero_enum")
estatus_enum = ENUM("Activo", "Inactivo", name="estatus_enum")

usuario = Table(
    "usuario",
    meta,
    Column("ID", Integer, primary_key=True, autoincrement=True, nullable=False),
    Column("Nombre", String(45), nullable=False),
    Column("Genero", genero_enum, nullable=False),
    Column("Peso", Float, nullable=False),
    Column("Talla", Float, nullable=False),
    Column("Fecha_Nacimiento", Date, nullable=False),
    Column("Estatus", estatus_enum, nullable=False, default="Activo"),
    Column(
        "Fecha_Registro", DateTime, nullable=False, default=datetime.datetime.utcnow
    ),
    Column("Fecha_Actualizacion", DateTime, nullable=True, default=None),
)

meta.create_all(engine)
