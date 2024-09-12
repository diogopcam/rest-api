from flask import Flask, json

app = Flask(__name__)

@app.route('/pinto', methods=['GET'])
def checkHealth():
    return 'Servidor está funcionando!'

if __name__ == '__main__':
    app.run(debug=True)

# @app.route('/allCandidates', method=['GET'])
# def getAllCandidates():
