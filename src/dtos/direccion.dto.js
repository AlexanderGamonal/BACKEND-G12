import Joi from 'joi';

export const direccionDto = Joi.object({
    calle: Joi.string().required(),
    numero: Joi.number().integer().required(),
    referencia: Joi.string(),
    departamento: Joi.string(),
})