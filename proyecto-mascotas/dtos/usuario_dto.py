from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.usuarios_model import UsuarioModel


# DTO > Data Transfer Object
class UsuarioResponseDto(SQLAlchemyAutoSchema):
    class Meta:
        # Sirve para pasar metadatos (informacion adicional) a la clase de la cual estoy heredando sin la necesidad de modificarla directamenre o llamar a sus metodos directamente
        model = UsuarioModel


class UsuarioRequestDto(SQLAlchemyAutoSchema):
    class Meta:
        # Sirve para pasar metadatos (informacion adicional) a la clase de la cual estoy heredando sin la necesidad de modificarla directamenre o llamar a sus metodos directamente
        model = UsuarioModel
