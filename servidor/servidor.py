from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/hello')
def hello():
    return jsonify({"mensaje": "Hola! Soy el Contenedor Servidor en Mac M1"})

@app.route('/time')
def time():
    ahora = datetime.now().strftime("%H:%M:%S")
    return jsonify({"hora_actual": ahora})

if __name__ == '__main__':
    # Escuchamos en el puerto 5000 INTERNO del contenedor
    app.run(host='0.0.0.0', port=5000)

