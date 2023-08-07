from sqlalchemy import Table, Column, Integer, String, Enum, DateTime, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Enum, Float, Date, DateTime
from sqlalchemy.dialects.mysql import ENUM
from config.db import meta, engine
from enum import Enum as PyEnum
import datetime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base



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
    Column("Valor_calorico",Integer, nullable=False, default=0),
    Column("Grupo_alimenticio", grupo_alimenticio_enum, nullable=False),
    Column("Estatus", Integer, nullable=False, default=1),
    Column("Fecha_Registro", DateTime, nullable=False, default=datetime.datetime.utcnow),
    Column("Fecha_Actualizacion", DateTime, nullable=True, default=None),
)


#Tabla componente y componente_has_alimento

UnidadMedidaEnum = ENUM(
    'g',
    'µg',
    'mg',
    'UI',
    'cal',
    'kcal',
    'ml',
    name="UnidadMedidaEnum"
)
componente = Table(
    'componente',
    meta,
    Column("ID",Integer, primary_key=True, autoincrement=True),
    Column("Nombre",String(50), nullable=False),
    Column("Componente_Padre",Integer, default=None),
    Column("Unidad_medida", UnidadMedidaEnum, nullable=False),
    Column("Estatus", Integer, nullable=False, default=1),
    Column("Fecha_Registro", DateTime, nullable=False, default=datetime.datetime.utcnow),
    Column("Fecha_Actualizacion", DateTime, nullable=True, default=None),
)

ComponenteHasAlimento = Table(
    'componente_has_alimento',
    meta,
    Column("componente_ID", Integer, ForeignKey('componente.ID'), primary_key=True),
    Column("alimento_ID", Integer, ForeignKey('alimento.ID'), primary_key=True),
    Column("Fecha_Inicio", DateTime, nullable=False),
    Column("Fecha_Fin", DateTime, nullable=False)
)



# Crear las tablas en la base de datos
meta.create_all(engine)