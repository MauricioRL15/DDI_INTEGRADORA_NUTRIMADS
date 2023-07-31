from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Enum, Float, Date, DateTime
from sqlalchemy.dialects.mysql import ENUM
from config.db import meta, engine
import datetime

'''
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
'''

# Definición del enumerador para la columna "Genero"
genero_enum = ENUM("Femenino", "Masculino", "No_Binario", name="genero_enum")

# Definición del enumerador para la columna "Estatus"
estatus_enum = Enum("Activo", "Inactivo", name="estatus_enum")

# Tabla Usuario
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
    Column("Fecha_Registro", DateTime, nullable=False, default=datetime.datetime.utcnow),
    Column("Fecha_Actualizacion", DateTime, nullable=True, default=None),
)

# Tabla Alimento
cantidad_enum = ENUM("Pieza", "g", name="cantidad_enum")

grupo_alimenticio_enum = ENUM(
    "Fruta", "Verdura", "Cereal", "Leguminosa", "Origen_animal", name="grupo_alimenticio_enum"
)

alimento = Table(
    "alimento",
    meta,
    Column("ID", Integer, primary_key=True, autoincrement=True, nullable=False),
    Column("Nombre", String(25), nullable=False),
    Column("Cantidad", cantidad_enum, nullable=False),
    Column("Grupo_alimenticio", grupo_alimenticio_enum, nullable=False),
    Column("Estatus", Integer, nullable=False, default=1),
    Column("Fecha_Registro", DateTime, nullable=False, default=datetime.datetime.utcnow),
    Column("Fecha_Actualizacion", DateTime, nullable=True, default=None),
)

# Crear las tablas en la base de datos
meta.create_all(engine)