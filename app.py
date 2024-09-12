from flask import Flask, jsonify
from controller.CandidateController import candidate_bp

app = Flask(__name__)

app.register_blueprint(candidate_bp)

if __name__ == '__main__':
    app.run(debug=True)
