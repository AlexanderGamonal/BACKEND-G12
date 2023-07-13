import { Router } from 'express'
import * as ProductoController from '../controllers/producto.controller.js'
import multer from 'multer'
import { v4 } from 'uuid'

const almacenamiento = multer.diskStorage({
    // como se va a llamar
    filename: (req, archivo, cb) => {
        // console.log(archivo.originalname)
        const nombre = `${v4()}-${archivo.originalname}`
        cb(null, nombre)
    },
    // donde se va a guardar
    destination: (req, file, cb) => {
        cb(null, './imagenes')
    }
})

export const productoRouter = Router()
const middlewareMulter = multer({
    storage: almacenamiento,
})

// single('nombreCampo') > aceptara solo un archivo en ese nombreCampo y este se guardara en req.file
// array('nombreCampo', cantidadElementos) > aceptara un arreglo (varios) archivos en ese nombreCampo y la cantidad para indicar cuantos elementos puede aceptar como maximo
// field('campos') > aceptara varios campos especificados en campos en el cual se aceptaran archivos o textos
// none() > solamente aceptara textos y no archivos
// any() > acepta tanto archivos como textos, si hay varios archivos estos se almacenaran en req.files
productoRouter.route('/productos').post(middlewareMulter.single('imagen'), ProductoController.crearProducto)

productoRouter.get('/devolver-imagen/:nombre', ProductoController.devolverImagenLocal)

productoRouter.get('/producto/:id', ProductoController.devolverProducto)