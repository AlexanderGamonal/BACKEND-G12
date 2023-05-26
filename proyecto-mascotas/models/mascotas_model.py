from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy import types
from base_de_datos import conexion
from enum import Enum


class SexoEnum(Enum):
    Macho = "Macho"
    Hembra = "Hembra"
    Otro = "Otro"


class MascotasModel(conexion.Model):
    id = Column(type_=types.Integer, autoincrement=True, primary_key=True)
    nombre = Column(type_=types.Text, nullable=False)
    apellido = Column(type_=types.Text, nullable=True)
    sexo = Column(type_=types.Enum(SexoEnum), default=SexoEnum.Otro, nullable=False)
    fechaNacimiento = Column(type_=types.Date, name="fecha_nacimiento", nullable=False)
    raza = Column(type_=types.Text, default="otro")
    # relacion nuestra tabla usuarios con mascotas
    usuarioId = Column(
        ForeignKey(column="usuarios.id"),
        type_=types.Integer,
        nullable=False,
        name="usuario_id",
    )

    __tablename__ = "mascotas"
