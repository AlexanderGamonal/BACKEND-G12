from flask_restful import Resource, reqparse
from models.models import Area, Empleado
from data_base import db
from dtos.dtos import AreaSchema, EmpleadoSchema


class AreaResource(Resource):
    def get(self):
        areas = Area.query.all()
        areas_schema = AreaSchema(many=True)
        result = areas_schema.dump(areas)
        return result

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("nombre", type=str, required=True)
        parser.add_argument("piso", type=int, required=True)
        data = parser.parse_args()
        area = Area(**data)
        db.session.add(area)
        db.session.commit()
        area_schema = AreaSchema()
        result = area_schema.dump(area)
        return result


class AreaDetailResource(Resource):
    def get(self, id):
        area = Area.query.get(id)
        if area is None:
            return {"message": "Area no encontrada"}, 404
        area_schema = AreaSchema()
        result = area_schema.dump(area)
        return result


class EmpleadoResource(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("email", type=str)
        parser.add_argument("nombre", type=str)
        data = parser.parse_args()
        if data["email"] is not None:
            empleados = Empleado.query.filter_by(email=data["email"]).all()
        elif data["nombre"] is not None:
            empleados = Empleado.query.filter(
                or_(
                    Empleado.nombre.like(f'%{data["nombre"]}%'),
                    Empleado.apellido.like(f'%{data["nombre"]}%'),
                )
            ).all()
        else:
            empleados = Empleado.query.all()
        empleados_schema = EmpleadoSchema(many=True)
        result = empleados_schema.dump(empleados)
        return result

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("nombre", type=str, required=True)
        parser.add_argument("apellido", type=str, required=True)
        parser.add_argument("email", type=str, required=True)
        parser.add_argument("area_id", type=int, required=True)
        data = parser.parse_args()
        empleado = Empleado(**data)
        db.session.add(empleado)
        db.session.commit()
        empleado_schema = EmpleadoSchema()
        result = empleado_schema.dump(empleado)
        return result
