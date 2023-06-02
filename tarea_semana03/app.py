from flask import Flask
from flask_restful import Api
from data_base import init_db
from controllers.controller import AreaResource, AreaDetailResource, EmpleadoResource
from flask_migrate import Migrate
from data_base import db

app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://postgres:password@localhost:5432/mi_empresa"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
api = Api(app)

migrate = Migrate(app, db)

init_db(app)

api.add_resource(AreaResource, "/areas")
api.add_resource(AreaDetailResource, "/area/<int:id>")
api.add_resource(EmpleadoResource, "/empleados")

if __name__ == "__main__":
    app.run(debug=True)
