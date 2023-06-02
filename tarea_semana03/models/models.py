from data_base import db


class Area(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=True, nullable=False)
    piso = db.Column(db.Integer, nullable=False)


class Empleado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    area_id = db.Column(db.Integer, db.ForeignKey("area.id"), nullable=False)
    area = db.relationship("Area", backref=db.backref("empleados", lazy=True))
