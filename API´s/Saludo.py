from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/saludar', methods=['POST'])
def saludar():
    data = request.get_json()  # Obtener los datos enviados desde el frontend (JSON)
    name = data.get('name')  # Extraer el nombre

    if name:
        greeting = f"Hola, {name}!"
    else:
        greeting = "¡Hola, invitado!"

    return jsonify({'greeting': greeting})


if __name__ == '__main__':
    app.run(debug=True)
