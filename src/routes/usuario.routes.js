import * as UsuarioController from '../controllers/usuario.controller.js';
import { Router } from 'express';
import { validarToken } from '../utils/validador.js';

//Utilizamos la interfaz express para poder usar las rutas
export const usuarioRouter = Router();

// Creamos la ruta para registrar un usuario
usuarioRouter.post('/registro', UsuarioController.registroUsuario);
usuarioRouter.post('/login', UsuarioController.login);
// por q si en el validadorToken llega a next pasa a controlador final(perfil) 
usuarioRouter.get('/perfil', validarToken, UsuarioController.perfil);

