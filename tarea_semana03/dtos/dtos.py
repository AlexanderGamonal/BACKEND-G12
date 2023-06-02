from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.models import Area, Empleado


class AreaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Area


class EmpleadoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Empleado
