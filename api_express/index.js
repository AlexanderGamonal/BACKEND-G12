import express from "express";
import Joi from "joi";
import swaggerUI from "swagger-ui-express";
//indica el tipo de informacion que tendremos en nuestra importacion
import swaggerDoc from './swagger.json' assert { type: "json" }; 

const servidor = express();

const productos = [];

const productoValidator = Joi.object({
  nombre: Joi.string().required().min(5).message("error, faltan caracteres"),
  precio: Joi.number().required().min(0),
  descripcion: Joi.string().optional(),
});

// indicar middleware(intermediario)
// ahora nuestra aplicacion de express entendera y convertira la informacion entrante a JSON (application/json)
servidor.use(express.json());
//tipo form-url-encoded (application/form-urlencoded)
// servidor.use(express.urlencoded());

servidor.use('/docs', swaggerUI.serve, swaggerUI.setup(swaggerDoc));

servidor.get("/inicio", (req, res) => {
  res.status(200).json({
    message: "Bienvenido a mi API en Express",
  });
});

servidor
  .post("/productos", (req, res) => {
    console.log(req.body);
    // const body = req.body;
    const { body } = req;

    const validacion = productoValidator.validate(body);
    console.log(validacion);

    if (validacion.error) {
      return res.status(400).json({
        message: "Error al crear el producto",
        error: validacion.error.details[0].message,
      });
    } else {
      productos.push(validacion.value);
      res.status(201).json({
        message: "Producto creado exitosamente",
      });
    }

    productos.push();
    res.status(201).json({
      message: "Producto creado exitosamente",
    });
  }).get("/productos", (req, res) => {
    res.json({
      content: productos,
    });
  });

servidor
  .route("/productos/:id")
  .get((req, res) => {
    console.log(req.params);
    const { id } = req.params;
    const resultado = productos[id];
    console.log(resultado);
    if (!resultado) {
      return res.status(404).json({
        message: "El producto no existe",
      });
    } else {
      return res.json({
        content: resultado,
      });
    }
  })
  .put((req, res) => {
    const id = req.params.id;
    const body = req.body;
    const productoEncontrado = productos[id];

    if (!productoEncontrado) {
      return res.status(404).json({
        message: "El producto no existe",
      });
    }

    //si es q existe el producto
    const validacion = productoValidator.validate(body);

    if (validacion.error) {
      return res.status(400).json({
        message: "Error al actualizar el producto",
        error: validacion.error.details[0].message,
      });
    } else {
      productos[id] = validacion.value;
      return res.json({
        message: "Producto actualizado exitosamente",
      });
    }
  })
  .delete((req, res) => {
    const { id } = req.params;
    const productoEncontrado = productos[id];
    if (!productoEncontrado) {
      return res.status(404).json({
        message: "El producto no existe",
      });
    }
    // si es q existe el producto cambiar su valor a null
    productos[id] = null;

    // retornar el mensaje
    return res.json({
      message: "Producto eliminado exitosamente",
    });
  });

servidor.listen(3000, () => {
  console.log("Servidor corriendo exitosamente");
});
