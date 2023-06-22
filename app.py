from flask import Flask
from flask_restful import Api
from dotenv import load_dotenv
from config import conexion
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from controllers.usuario_controller import RegistroController, LoginController, PerfilController
from controllers.publicacion_controller import PublicacionesController, PublicacionController
from datetime import timedelta
from os import environ  # muestra las variables de entorno
# las variables de entorno son variables que estan presentes de manera GLOBAL en toda la maquina / servidor y es aca donde se suelen guardar las credenciales (a la bd, informacion a otras API's, mensajeria (emails), entro otros), credenciales sensibles que no deben ser expuestas

# load_dotenv > carga todas las variables presentes en el archivo .env y las coloca como si fuesen variables de entorno, SIEMPRE debe ir en la primera linea del archivo principal del proyecto
load_dotenv()

# instancias
app = Flask(__name__)
api = Api(app)
app.config['JWT_SECRET_KEY'] = environ.get('SECRET_KEY')
# https://flask-jwt-extended.readthedocs.io/en/stable/options.html#jwt-access-token-expires
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1, minutes=30)
# busca en la variable config la variable JWT_SECRET_KEY > sera el secreto por el cual se generaran las tokens
jwt = JWTManager(app)


@jwt.unauthorized_loader
def tokenRequerida(razon):
    # Ingresara aca si no se proveyo una tokenq a un endpoint que si necesita
    print(razon)
    return {
        'message': 'Se necesita una token para realizar esta accion'
    }, 401


@jwt.invalid_token_loader
def tokenInvalida(razon):
    # ingresara aca si es que la token proveida no es correcta
    print(razon)
    message = ''
    if razon == 'Not enough segments':
        message = 'La token tiene que tener 3 segmentos, el header, payload y signature'

    elif razon == "Invalid header string: 'utf-8' codec can't decode byte 0xc7 in position 0: invalid continuation byte":
        message = 'Token invalida'

    elif razon == 'Signature verification failed':
        message = 'Esta token no pertenece a esta API'

    return {
        'message': message
    }, 401

# el metodo get de los diccionarios intentara buscar esa llave y si no existe, retornara None, a diferencia de las [] (llaves) que si no encuentra emitira un error de tipo KeyError
# el metodo .get() solamente se puede utilizar para devolver o visualizar los valores, mas no para asignar mientras que las llaves [] son para lectura y escritura


app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')
# app.config['SQLALCHEMY_DATABASE_URI'] = environ['DATABASE_URL']

conexion.init_app(app)

Migrate(app, conexion)

# declaramos las rutas
api.add_resource(RegistroController, '/registro-usuario')
api.add_resource(LoginController, '/login')
api.add_resource(PerfilController, '/perfil')
api.add_resource(PublicacionesController, '/publicaciones')
api.add_resource(PublicacionController, '/publicacion/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
