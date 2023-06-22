from sqlalchemy import Column, types, ForeignKey
from config import conexion


class Publicacion(conexion.Model):
    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    titulo = Column(type_=types.Text, nullable=False)
    descripcion = Column(type_=types.Text)
    habilitado = Column(type_=types.Boolean, default=True)
    usuarioId = Column(ForeignKey(column='usuarios.id'),
                       nullable=False, name='usuario_id')

    __tablename__ = 'publicaciones'
