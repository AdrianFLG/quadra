from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Bienvenido a Quadra</h1><p>Tu app para calificar puestos de comida callejera</p>"

if __name__ == '__main__':
    app.run(debug=True)
