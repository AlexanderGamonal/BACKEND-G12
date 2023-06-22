import pytest
from testing.prueba import sumar


def test_sumar():
    a = 10
    b = 40
    resultado = sumar(a, b)
    assert resultado == 50


def test_sumar_erroneo():
    resultado = sumar(10, 80)
    assert resultado != 100


def test_sumar_exception():
    with pytest.raises(TypeError) as error:
        resultado = sumar('A', 50)
        assert resultado == None
    assert error.errisinstance(TypeError)
    assert error.value.args[0] == 'can only concatenate str (not "int") to str'
