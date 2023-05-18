from flask import Flask;

app = Flask(__name__)

@app.route('/productos')
def gestionProductos():
    return 'Yo soy la gestion de los productos'

if __name__ == "__main__":
    app.run()
