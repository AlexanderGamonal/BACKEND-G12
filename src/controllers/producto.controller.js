import { conexion } from '../base_de_datos.js'
import fs from 'fs' // file system
import path from 'path'
import { fileURLToPath } from 'url';
import S3 from 'aws-sdk/clients/s3.js'
import { Prisma } from '@prisma/client'

const conexionS3 = new S3({
    region: process.env.AWS_BUCKET_REGION,
    credentials: {
        accessKeyId: process.env.AWS_ACCESS_KEY,
        secretAccessKey: process.env.AWS_SECRET_KEY
    }
})


export const crearProducto = async (req, res) => {
    const { body, file } = req
    // console.log(file)

    // subir imagen a s3
    const lecturaArchivo = fs.createReadStream(file.path)

    const resultado = await conexionS3.upload({
        Bucket: process.env.AWS_BUCKET_NAME, // el bucket al cual subire mi archivo
        Body: lecturaArchivo, // es el contenido del archivo
        Key: file.filename // nombre del archivo con el que se guardara en el bucket
    }).promise()

    await conexion.producto.create({
        data: {
            // Agregar el dto del producto para validar la informacion EXCEPTO LA IMAGEN
            precio: +body.precio,
            disponible: body.disponible === 'true' ? true : false,
            nombre: body.nombre,
            imagen: resultado.Key
        }
    })
    // console.log(resultado)

    return res.json({
        message: 'Producto creado exitosamente'
    })
}

export const devolverProducto = async (req, res) => {
    const { id } = req.params

    try {
        const productoEncontrado = await conexion.producto.findUniqueOrThrow({ where: { id: +id } })

        const urlFirmada = conexionS3.getSignedUrl('getObject', {
            Key: productoEncontrado.imagen,
            Bucket: process.env.AWS_BUCKET_NAME,
            Expires: 15 // cuanto durara la url hasta que deje de ser valida
        },)


        return res.json({
            content: { ...productoEncontrado, imagen: urlFirmada }
        })
    } catch (error) {
        if (error instanceof Prisma.PrismaClientKnownRequestError) {
            return res.status(404).json({
                message: 'El producto no exite'
            })
        }
    }
}

export const eliminarProducto = async (req, res) => {
    // TODO: Eliminar el producto de la base de datos PERO primero eliminarlo del bucket de s3
    const { id } = req.params
    // Busquen el producto en la base de datos y obtengan su key

    await conexionS3.deleteObject({
        Key: '',
        Bucket: '',

    }).promise()
    // Proceder a eliminarlo de la base de datos

}

export const devolverImagenLocal = async (req, res) => {
    const { nombre } = req.params

    try {
        const __filename = fileURLToPath(import.meta.url);
        const __dirname = path.dirname(__filename);
        // leemos el archivo para ver si existe, si no existe emitira un error
        const ubicacion = path.join(__dirname, '../../imagenes', nombre)
        fs.readFileSync(ubicacion)

        return res.sendFile(ubicacion)
    } catch (error) {
        return res.status(404).json({
            message: 'El archivo no existe',
            content: error.message
        })
    }

}