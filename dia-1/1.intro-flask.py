from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(
    app,
    origins=["http://localhost:5500", "http://127.0.0.1:5500"],
    methods=["GET", "POST", "PUT", "DELETE"],
)

productos = [
    {"id": 1, "nombre": "Martillo", "precio": 15.8, "disponible": True},
    {"id": 2, "nombre": "Serrucho", "precio": 20.5, "disponible": True},
    {"id": 3, "nombre": "Taladro", "precio": 120.0, "disponible": False},
]


@app.route("/productos", methods=["GET", "POST"])
def gestionProductos():
    print(request.method)
    if request.method == "GET":
        productos_existentes = []
        for producto in productos:
            if producto is None:
                continue
            productos_existentes.append(producto)
        return {"message": "Los productos son", "content": productos_existentes}

    elif request.method == "POST":
        print(request.json)
        id = len(productos) + 1
        data = request.json
        data["id"] = id
        productos.append(data)

        return {"message": "Producto creado exitosamente"}


@app.route("/producto/<int:id>", methods=["GET", "PUT", "DELETE"])
def gestionProducto(id):
    print(id)
    resultado = None
    for producto in productos:
        if producto is None:
            continue
        if producto["id"] == id:
            resultado = producto
            break

    if resultado == None:
        return {"message": "No se encontro el producto a buscar"}

    if request.method == "GET":
        return {"message": "El producto es", "content": resultado}

    elif request.method == "PUT":
        data = request.json
        productos[id - 1] = data
        productos[id - 1]["id"] = id

        return {"message": "Producto actualizado exitosamente"}

    elif request.method == "DELETE":
        productos[id - 1] = None

        return {"message": "Producto eliminado correctamente"}


if __name__ == "__main__":
    app.run(debug=True)
