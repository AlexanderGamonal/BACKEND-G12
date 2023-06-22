from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from models.usuario_model import Usuario, SexoUsuario, TipoUsuario
from marshmallow import Schema, fields
from marshmallow_enum import EnumField


class RegistroUsuarioRequestDto(SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario


class UsuarioResponseDto(SQLAlchemyAutoSchema):
    sexo = EnumField(enum=SexoUsuario, by_value=True)
    tipoUsuario = EnumField(enum=TipoUsuario, by_value=True)
    # auto_field > utilizara los mismos parametros que la clase Field de marshmallow para modificar su comportamiento dentro del DTO, OJO!!! Esto no modifica en nada las propiedades dentro del modelo SOLO dentro del DTO
    # Si no queremos que se utilice para devolver la data y solamente para validarla entonces utilizamos el parametro load_only, Si en el caso solo quisieramos devolver la data pero no validarla entonces utilizariamos el metodo dump_only
    password = auto_field(load_only=True)
    id = auto_field(load_only=True)

    class Meta:
        model = Usuario


class LoginUsuarioRequestDto(Schema):
    # https://marshmallow.readthedocs.io/en/stable/marshmallow.fields.html
    email = fields.Email(required=True)
    password = fields.String(required=True)
