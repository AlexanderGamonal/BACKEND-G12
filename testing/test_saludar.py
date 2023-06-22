import testing.prueba


def mock_saludoCordial():
    return 'Holaa'


def test_saludar(monkeypatch):
    # monkeypatch > me dara toda la informacion de donde estoy haciendo el testing
    print(monkeypatch)
    # setattr > primer parametro le diremos que queremos modificar (archivo o un modulo), segundo parametro indicaremos que funcion o metodo queremos modificar, tercer parametro el nuevo comportamiento de el segundo parametro indicado
    monkeypatch.setattr(testing.prueba, 'saludoCordial', mock_saludoCordial)
    resultado = testing.prueba.saludar()

    assert resultado == 'Holaa'


def test_saludar_con_cordialidad():
    resultado = testing.prueba.saludar()

    assert resultado == 'Muy buenas noches ante ustedes'
