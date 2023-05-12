meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo']

for mes in meses:
    print('El mes es:')
    print(mes)


for numero in range(5):
    print('El numero es:')
    print(numero)

for numero in range(2, 10):
    print('El numero es:')
    print(numero)

print('---------------------------------------')

for numero in range(20,0,-3):
    print(numero)


print('---------------------------------------')

# while > mientras
tope = 0
while(tope < 100):
    print('El tope es {}'.format(tope))
    tope += 1

# condicionales
persona = 'Eduardo'
nacionalidad = 'Uruguayo'
print(persona == 'Eduardo')
print(persona != 'Eduardo')
print(persona == 'Eduardo' and nacionalidad == 'Peruano')
print(persona == 'Eduardo' or nacionalidad == 'Peruano')





