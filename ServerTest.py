from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'message': 'Servidor está funfando!'})

if __name__ == '__main__':
    app.run(debug=True)
