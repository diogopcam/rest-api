from flask import Flask, json, Blueprint, request, jsonify

from services.CandidateService import CandidateService

candidate_bp = Blueprint('candidate_bp', __name__)
candidate_service = CandidateService()

@candidate_bp.route('/ping', methods=['GET'])
def checkHealth():
    return 'Servidor está funcionando!'

@candidate_bp.route('/getAllCandidates', methods=['GET'])
def obter_dados():
    dados = candidate_service.obter_dados()
    print(dados)
    dados_flask = dados.to_dict(orient='records')
    return jsonify(dados_flask)

