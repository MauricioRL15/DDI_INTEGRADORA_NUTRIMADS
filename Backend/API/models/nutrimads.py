from sqlalchemy import Table, Column, Integer, String, Enum, DateTime, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Enum, Float, Date, DateTime
from sqlalchemy.dialects.mysql import ENUM
from config.db import meta, engine
from enum import Enum as PyEnum
import datetime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


# Todos los ENUMS los DEFINIMOS
cantidad_enum = Enum('Pieza', 'g', name='cantidad_enum')
unidad_medida_enum = Enum('g', 'µg', 'mg', 'UI', 'cal', 'kcal', 'ml', '%', 'mcg', name='unidad_medida_enum')
grupo_alimenticio_enum = Enum('Fruta', 'Verdura', 'Cereal', 'Leguminosa', 'Origen_animal', name='grupo_alimenticio_enum')
estatus_enum = Enum('Activo', 'Inactivo', name='estatus_enum')
genero_enum = Enum('Femenino', 'Masculino', 'No_Binario', name='genero_enum')
tipo_consumo_enum = Enum('Consumo_realizado', 'Consumo_Sugerido', name='tipo_consumo_enum')
factor_estatus_enum = Enum('Temprano', 'Estable', 'Grave', name='factor_estatus_enum')
criterio_estatus_enum = Enum('Saludable', 'No_saludable', name='criterio_estatus_enum')



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
alimento = Table(
    "alimento",
    meta,
    Column("ID", Integer, primary_key=True, autoincrement=True, nullable=False),
    Column("Nombre", String(25), nullable=False),
    Column("Cantidad", cantidad_enum, nullable=False),
    # Column("Valor_calorico",Integer, nullable=False, default=0),
    Column("Grupo_alimenticio", grupo_alimenticio_enum, nullable=False),
    Column("Estatus", Integer, nullable=False, default=1),
    Column("Fecha_Registro", DateTime, nullable=False, default=datetime.datetime.utcnow),
    Column("Fecha_Actualizacion", DateTime, nullable=True, default=None),
)


#Tabla componente
componente = Table(
    'componente',
    meta,
    Column("ID",Integer, primary_key=True, autoincrement=True, nullable=False),
    Column("Nombre",String(50), nullable=False),
    Column("Cantidad",Integer, nullable=False),
    Column("Unidad_medida", unidad_medida_enum, nullable=False),
    Column("Estatus", Integer, nullable=False, default=1),
    Column("Fecha_Registro", DateTime, nullable=False, default=datetime.datetime.utcnow),
    Column("Fecha_Actualizacion", DateTime, nullable=True, default=None),
    Column("Componente_Padre",String(25), default=None)
)

# Tabla componente_has_alimento
ComponenteHasAlimento = Table(
    'componente_has_alimento',
    meta,
    Column("componente_ID", Integer, ForeignKey('componente.ID'), primary_key=True),
    Column("alimento_ID", Integer, ForeignKey('alimento.ID'), primary_key=True),
    Column("Fecha_Inicio", DateTime, nullable=False),
    Column("Fecha_Fin", DateTime, nullable=False)
)

#Tabla Consumo 
consumo = Table(
    'consumo',
    meta,
    Column('ID', Integer, primary_key=True, autoincrement=True),
    Column('Cantidad', Float, nullable=False),
    Column('Tipo', tipo_consumo_enum, nullable=False),
    Column("Estatus", Integer, nullable=False, default=1),
    Column('Fecha_Registro', DateTime, nullable=False),
    Column('Fecha_Actualizacion', DateTime, nullable=True),
    Column('Usuario_ID', Integer, ForeignKey('usuario.ID'), nullable=False),
)

# Tabla Rol
rol = Table(
    'rol',
    meta,
    Column('ID', Integer, primary_key=True, autoincrement=True),
    Column('Nombre', String(50), nullable=False),
    Column('Descripcion', String(150), nullable=False),
    Column('Estatus', estatus_enum, nullable=False, default='Activo'),
    Column('Fecha_Registro', DateTime, nullable=False),
    Column('Fecha_Actualizacion', DateTime, nullable=True)
)

# Tabla Usuario_has_Rol
usuario_has_rol = Table(
    'usuario_has_rol',
    meta,
    Column('usuario_ID', Integer, ForeignKey('usuario.ID'), primary_key=True),
    Column('rol_ID', Integer, ForeignKey('rol.ID'), primary_key=True),
    Column('Fecha_Inicio', DateTime, nullable=False),
    Column('Fecha_Fin', DateTime, nullable=False),
)

# Tabla Alimento_has_Criterio
alimento_has_criterio = Table(
    'alimento_has_criterio',
    meta,
    Column('alimento_ID', Integer, ForeignKey('alimento.ID'), primary_key=True),
    Column('criterio_ID', Integer, ForeignKey('criterio.ID'), primary_key=True),
    Column('Fecha_Inicio', DateTime, nullable=False),
    Column('Fecha_Fin', DateTime, nullable=False),
)

# Tabla Consumo_has_Alimento
consumo_has_alimento = Table(
    'consumo_has_alimento',
    meta,
    Column('Consumo_ID', Integer, ForeignKey('consumo.ID'), primary_key=True),
    Column('Alimento_ID', Integer, ForeignKey('alimento.ID'), primary_key=True),
    Column('Fecha_Inicio', DateTime, nullable=False),
    Column('Fecha_Fin', DateTime, nullable=False),
)

# Tabla Criterio
criterio = Table(
    'criterio',
    meta,
    Column('ID', Integer, primary_key=True, autoincrement=True),
    Column('Nombre', String(65), nullable=False),
    Column('Descripcion', String(200), nullable=False),
    Column('Valor_Maximo', Float, nullable=False),
    Column('Valor_Minimo', Float, nullable=False),
    Column('Estatus', criterio_estatus_enum, nullable=False, default='Saludable'),
    Column('Fecha_Registro', DateTime, nullable=False),
    Column('Fecha_Actualizacion', DateTime, nullable=True),
)

# Tabla Criterio_has_Usuario
criterio_has_usuario = Table(
    'criterio_has_usuario',
    meta,
    Column('criterio_ID', Integer, ForeignKey('criterio.ID'), primary_key=True),
    Column('usuario_ID', Integer, ForeignKey('usuario.ID'), primary_key=True),
    Column('Fecha_Inicio', DateTime, nullable=False),
    Column('Fecha_Fin', DateTime, nullable=False),
)

# Tabla Factor
factor = Table(
    'factor',
    meta,
    Column('ID', Integer, primary_key=True, autoincrement=True),
    Column('Nombre', String(50), nullable=False),
    Column('Estatus', factor_estatus_enum, nullable=False, default='Temprano'),
    Column('Fecha_Registro', DateTime, nullable=False),
    Column('Fecha_Actualizacion', DateTime, nullable=True),
)

# Tabla Factor_has_Componente
factor_has_componente = Table(
    'factor_has_componente',
    meta,
    Column('factor_ID', Integer, ForeignKey('factor.ID'), primary_key=True),
    Column('componente_ID', Integer, ForeignKey('componente.ID'), primary_key=True),
    Column('Fecha_Inicio', DateTime, nullable=False),
    Column('Fecha_Fin', DateTime, nullable=False),
)

# Tabla Factor_has_Usuario
factor_has_usuario = Table(
    'factor_has_usuario',
    meta,
    Column('factor_ID', Integer, ForeignKey('factor.ID'), primary_key=True),
    Column('usuario_ID', Integer, ForeignKey('usuario.ID'), primary_key=True),
    Column('Fecha_Inicio', DateTime, nullable=False),
    Column('Fecha_Fin', DateTime, nullable=False),
)

# Crear las tablas en la base de datos
meta.create_all(engine)