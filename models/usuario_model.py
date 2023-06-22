from config import conexion
from sqlalchemy import Column, types
from enum import Enum


class SexoUsuario(Enum):
    MASCULINO = 'MASCULINO'
    FEMENINO = 'FEMENINO'
    OTRO = 'OTRO'


class TipoUsuario(Enum):
    ADMINISTRADOR = 'ADMINISTRADOR'
    MEDICO = 'MEDICO'
    USUARIO = 'USUARIO'


class Usuario(conexion.Model):
    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    nombre = Column(type_=types.Text, nullable=False)
    apellido = Column(type_=types.Text)
    especialidad = Column(type_=types.Text, nullable=False)
    sexo = Column(type_=types.Enum(SexoUsuario), nullable=False)
    celular = Column(type_=types.Text)
    consultorio = Column(type_=types.Text, nullable=False)
    email = Column(type_=types.Text, nullable=False, unique=True)
    password = Column(type_=types.Text)
    tipoUsuario = Column(type_=types.Enum(TipoUsuario),
                         default=TipoUsuario.USUARIO, name='tipo_usuario')

    __tablename__ = 'usuarios'
