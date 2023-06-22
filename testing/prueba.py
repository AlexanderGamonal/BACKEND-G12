import requests


def sumar(a, b):
    return a + b


def saludar():
    print('holaaaaa')
    saludo = saludoCordial()
    return saludo


def saludoCordial():
    return 'Muy buenas noches ante ustedes'


def get_pokemones(nombre):
    resultado = requests.get(f'https://pokeapi.co/api/v2/pokemon/{nombre}')
    if resultado.status_code == 200:
        return resultado.json()

    else:
        return 'Error con la API'
