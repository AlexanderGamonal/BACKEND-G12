from flask_restful import Resource, request
from models.publicacion_model import Publicacion
from config import conexion
from flask_jwt_extended import get_jwt_identity, jwt_required
from dtos.publicacion_dto import PublicacionRequestDto, PublicacionResponseDto
from models.usuario_model import Usuario


class PublicacionesController(Resource):
    @jwt_required()
    def post(self):
        usuarioId = get_jwt_identity()
        dto = PublicacionRequestDto()
        try:
            dataValidada = dto.load(request.json)
            nuevaPublicacion = Publicacion(**dataValidada, usuarioId=usuarioId)

            conexion.session.add(nuevaPublicacion)
            conexion.session.commit()

            dtoRespuesta = PublicacionResponseDto()
            resultado = dtoRespuesta.dump(nuevaPublicacion)
            return {
                'message': 'Publicacion creada exitosamente',
                'content': resultado
            }, 201

        except Exception as e:
            conexion.session.rollback()
            return {
                'message': 'Error al crear la publicacion',
                'content': e.args
            }, 400

    def get(self):
        queryParams = request.args
        # print(request.args)
        # redundante
        # filtros = {}
        # if (queryParams.get('email')):
        #     filtros['email'] = queryParams.get('email')
        # -----

        # devolver todas las publicaciones que hay
        # No se recomienda utilizar la siguiente forma ya que pertenece al "legacy" de SQLAlchemy por lo que pronto puede estar en desuso
        # https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/legacy-query/
        # resultado = Publicacion.query.all()

        # Solamente necesito el ID
        # with_entities > especificar que columnas queremos extraer
        # SELECT * FROM ...
        # con el uso de with_entities
        # SELECT id, nombre FROM usuarios
        data = conexion.session.query(Usuario).with_entities(
            Usuario.id).filter_by(**queryParams).all()
        # data > [(1,), (2,)]
        print(data)
        usuariosIds = []
        for id in data:
            usuariosIds.append(id[0])
        # data = {'nombre': 'juan'}
        # data.k

        # SELECT * FROM publicaciones WHERE usuarioId = ...
        # SELECT * FROM publicaciones WHERE usuario_id IN (1,2);
        # https://www.postgresql.org/docs/current/functions-subquery.html#FUNCTIONS-SUBQUERY-IN

        resultado = conexion.session.query(
            Publicacion).filter(Publicacion.usuarioId.in_(usuariosIds)).all()

        dto = PublicacionResponseDto(many=True)
        publicaciones = dto.dump(resultado)
        return {
            'content': publicaciones
        }


class PublicacionController(Resource):
    # se encarga de 1. Validar que la token sea nuestra (concuerda el secreto),  2. De que la token aun no expiro, 3. Sea valida
    @jwt_required()
    # /publicacion/<int:id>
    def put(self, id):
        try:
            usuarioId = get_jwt_identity()
            # Buscar la publicacion segun el id y segun el usuarioId
            # SELECT * FROM publicaciones WHERE id = ... AND usuario_id = ....
            publicacion = conexion.session.query(Publicacion).filter_by(
                id=id, usuarioId=usuarioId).first()
            # publicacion = conexion.session.query(Publicacion).filter(Publicacion.id == id, Publicacion.usuarioId == usuarioId).first()
            if not publicacion:
                raise Exception('Publicacion no existe')

            dto = PublicacionRequestDto()
            dataValidada = dto.load(request.json)

            # Primera forma
            # publicacion.titulo = dataValidada.get('titulo')
            # publicacion.descripcion = dataValidada.get('descripcion')
            # publicacion.habilitado = dataValidada.get('habilitado')

            # Segunda forma
            # retornara la cantidad de registros actualizados
            conexion.session.query(Publicacion).filter_by(
                id=id, usuarioId=usuarioId).update(dataValidada)

            # Para guardar los cambios de manera permanente
            conexion.session.commit()
            resultado = PublicacionResponseDto().dump(publicacion)

            return {
                'message': 'Publicacion actualizada exitosamente',
                'content': resultado
            }, 201
        except Exception as e:
            return {
                'message': 'Error al actualizar la publicacion',
                'content': e.args
            }, 400

    @jwt_required()
    def delete(self, id):
        try:
            usuarioId = get_jwt_identity()
            # Primera Forma (forma mas optima)
            # Eliminar la publicacion usando el delete
            # DELETE FROM publicaciones WHERE id = ... AND usuario_id = ...;
            publicacionesEliminadas = conexion.session.query(
                Publicacion).filter_by(id=id, usuarioId=usuarioId).delete()

            if publicacionesEliminadas == 0:
                raise Exception('No se encontro la publicacion a eliminar')

            conexion.session.commit()

            # Segunda Forma
            # SELECT * FROM publicaciones WHERE id = ... AND usuario_id = ...;
            publicacionEncontrada = conexion.session.query(
                Publicacion).filter_by(id=id, usuarioId=usuarioId).first()

            if not publicacionEncontrada:
                raise Exception('No se encontro la publicacion a eliminar')

            # DELETE FROM ....
            conexion.session.delete(publicacionEncontrada)
            conexion.session.commit()
            return {
                'message': 'Publicacion eliminada exitosamente'
            }
        except Exception as e:
            return {
                'message': 'Error al eliminar la publicacion',
                'content': e.args
            }, 400
