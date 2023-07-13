import Joi from "joi";
import { TipoUsuario } from "@prisma/client";

export const  registroUsuarioDto = Joi.object({
    nombre: Joi.string().required(),
    apellido: Joi.string(),
    email: Joi.string().email().required(),
    password: Joi.string().required().regex(/^[a-zA-Z0-9!@#]{3,20}$/), //new RegExp('^[a-zA-Z0-9!@#]{3,20}$')
    tipoUsuario: Joi.string().regex(new RegExp(`${TipoUsuario.ADMIN}|${TipoUsuario.CLIENTE}`)).required()
});

export const loginDto = Joi.object({
    email: Joi.string().email().required(),
    password: Joi.string().required()
});

