from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.mascotas_model import MascotasModel


class MascotaRequestDto(SQLAlchemyAutoSchema):
    class Meta:
        model = MascotasModel
        # indicamos al DTO que tambien haga la validacion de las columnas que sean llaves foraneas
        include_fk = True
