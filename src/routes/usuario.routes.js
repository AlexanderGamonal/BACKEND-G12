import * as UsuarioController from '../controllers/usuario.controller.js';
import { Router } from 'express';

//Utilizamos la interfaz express para poder usar las rutas
export const usuarioRouter = Router();

// Creamos la ruta para registrar un usuario
usuarioRouter.post('/registro', UsuarioController.registroUsuario);

