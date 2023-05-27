from flask_restful import Resource, request
from base_de_datos import conexion
from models.usuarios_model import UsuarioModel
from dtos.usuario_dto import UsuarioResponseDto, UsuarioRequestDto


class UsuariosController(Resource):
    # cuando yo heredo la clase Resource ahora los metodos que yo cree con el mismo nombre de un metodo HTTP (GET, POST, PUT, DELETE) entonces ingresaran esos metodos.

    def get(self):
        # lista
        resultado = conexion.session.query(UsuarioModel).all()
        dto = UsuarioResponseDto(many=True)
        # dump > convierte la instancia de la clase en un resultado
        data = dto.dump(resultado)

        # print(resultado[0].nombre)
        # data = []
        # for usuario in resultado:
        #    data.append(
        #        {
        #            "id": usuario.id,
        #            "nombre": usuario.nombre,
        #            "apellido": usuario.apellido,
        #            "correo": usuario.correo,
        #            "dni": usuario.dni,
        #        }
        #    )
        return {"content": data}

    def post(self):
        data = request.json
        dto = UsuarioRequestDto()
        # load > valida el diccionario q le pasamos con los campos que cumplen las condiciones (requeridos, q sean del tipo de dato correcto)
        dataValidada = dto.load(data)
        print(dataValidada)
        # inicializo mi nuevo usuario
        nuevoUsuario = UsuarioModel(**dataValidada)
        # **dataValidada es para simplificar esto: nuevoUsuario = UsuarioModel(nombre = dataValidada.get('nombre), apellido = .....)
        # indicar que vamos a agregar un nuevo registro
        conexion.session.add(nuevoUsuario)
        try:
            # se usa para transaccion, sirve para indicar q todos los cambios de guarden de manera permanente, sino hacemos commit entonces no se guardara la informacion de manera permanente.
            conexion.session.commit()
            return {
                "message": "Usuario creado exitosamente"
            }, 201  # created (Creado Correctamente)
        except Exception as error:
            # rollback > Sirve para retroceder y dejar todos los posibles cambios sin efecto (los  incrementos, nuevos registros, actualizaciones y eliminaciones) quedan sin efecto.
            conexion.session.rollback()
            return (
                {
                    "message": "Error al crear el usuario",
                    "content": error.args,  # args > argumentos (porque fallo)
                },
            ), 400  # bad request(mala solicitud por parte del cliente)
