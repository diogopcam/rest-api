from flask import Flask, json, Blueprint, request, jsonify

candidate_bp = Blueprint('candidate_bp', __name__)

@candidate_bp.route('/ping', methods=['GET'])
def checkHealth():
    return 'Servidor está funcionando!'

