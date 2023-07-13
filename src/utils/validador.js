import jwt from 'jsonwebtoken';
import { conexion } from '../base_de_datos.js'

export function validarData({ error, message, data }) {
    // Si hay un error, emitiremos un error para detener el proceso
    if (error) {
        // La clase Error admite un mensaje que tiene que string, no puede JSON u otro tipo de dato por lo que convertimos nuestro json a un string utilizando el metodo stringify
        throw new Error(JSON.stringify({ message, content: error.details }))
    } else {
        // Si no hay error, retornaremos la data
        return data
    }
}

export async function validarToken(req, res, next) {
    // next > si todo esta bien le indicaremos que pase al siguiente middleware / controlador

    if (!req.headers.authorization) {
        // 403 > Forbidden
        return res.status(403).json({
            message: 'Se necesita un token para realizar esta peticion'
        })
    }

    // Bearer xxxxx.xxxxx.xxxxx
    const token = req.headers.authorization.split(' ')[1]

    if (!token) {
        return res.status(400).json({
            message: 'El formato tiene que ser "Bearer <YOUR_TOKEN>"'
        })
    }

    try {
        const payload = jwt.verify(token, process.env.JWT_SECRET)
        const usuario = await conexion.usuario.findUniqueOrThrow({ where: { id: payload.id } })
        // agrego esta propiedad a mi request para que se pueda reutilizar en los otros controladores
        req.user = usuario

        // next > pase al siguiente controlador
        next()
    } catch (error) {
        return res.status(403).json({
            message: 'Error en la token',
            content: error.message
        })
    }
}