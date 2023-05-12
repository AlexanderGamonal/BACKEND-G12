# listas(arrays)
notas = [10, 20, 25, 80]

variada = [10, 'Juana', 70.5, True, [1,2,3]]

print(notas[0])

# Si queremos ingresar una nueva posicion no se le coloca asignacion
# notas[4] = 40

# se utiliza el metodo append
# en js es push, en python es append
notas.append(40)

del notas[1]

print(notas)

# es que el pop los quita de la lista PERO nos devuelve el contenido eliminado

nota_eliminada : notas.pop(1)
print(notas)
print(nota_eliminada)

# le pasamos el contenido que queremos eliminar, y si existe lo eliminara, caso contrario lanzara error.
notas.remove(80)

# tupla
alumnos : ("Eduardo", "Roberto", "Juana", "Roxana")
# la diferencia es que la tupla no se puede modificar (es inmutable)
# la tupla se usa para difinir valores que nunca se modificaran en todo el ciclo de nuestro proyecto

print(alumnos[0])
# alumnos[0] : "Pepito"

# set(conjuntos)
# que es desordenada  y almacena la informacion de manera desordenada sin respetar los indices
mascotas : {'fido', 'iguana', 'gato'}
print(mascotas)
print(len(mascotas))
mascotas.add('mocha')
mascota_eliminada : mascotas.pop

print(mascota_eliminada)

# diccionarios
# es ordenada pero por llaves(no por posiciones)
persona = {
    'nombre': 'eduardo',
    'apellido': 'de rivero',
    'sexo': 'masculino',
    'hobbies': ['Jugar Futbol', 'Montar bici']
}

print(persona['nombre'])
print(persona.get('nacionalidad'))