from datetime import datetime

class Persona:
    nombre = 'Juan'
    edad = 28
    correo = 'jperez@gmail.com'
    peso = 89.5

    def decir_hora(self):
        hora_actual = datetime.now()
        data = hora_actual.strftime('%I-%p')
        hora, turno = data.split('-')
        # print(hora)
        # print(turno)
        if turno == 'PM':
            print('Son las {} de la noche'.format(hora))
        else:
            print('Son las {} de la mañana'.format(hora))

    
    def saludar(self):
        print('Hola! Soy {}'.format(self.nombre))


# variable pasa a llamarse instancia (copia de la clase que sera almacenada en esa variable)
persona1 = Persona()
persona1.nombre = 'Roberto'
persona1.saludar()
print(persona1.nombre)

persona2 = Persona()
print(persona2.nombre)
persona2.decir_hora()