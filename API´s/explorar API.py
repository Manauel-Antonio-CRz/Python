from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/endpoint')
def mi_endpoint():
    data = {"mensaje": "Hola desde la API"}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
