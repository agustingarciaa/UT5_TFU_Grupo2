from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "¡Hola, mundo!"

@app.route("/saludo/<nombre>")
def saludo(nombre):
    return f"Hola, {nombre}!"

if __name__ == "__main__":
    app.run(debug=True)