import Prisma from '@prisma/client';

// Variable encagada de conectarse a la base de datosy por aca haremos todas las consultas.
export const conexion = new Prisma.PrismaClient();