import pytest
from flask import Flask
from app import app


# hara que nuestra variable sea accesible durante todo el archivo
@pytest.fixture()
def cliente():
    # metodo que Flask brinda para poder hacer escenarios de testing y no levantara un servidor web como tal
    yield app.test_client()


def test_publicaciones_get(cliente):
    resultado = cliente.get('/publicaciones')
    assert resultado.status_code == 200
    assert resultado.json == {
        'content': []
    }
