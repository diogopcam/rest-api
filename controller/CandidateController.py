from flask import Flask, json, Blueprint, request, jsonify

from services.CandidateService import CandidateService

candidate_bp = Blueprint('candidate_bp', __name__)
candidate_service = CandidateService()

@candidate_bp.route('/ping', methods=['GET'])
def check_health():
    return 'Servidor está funcionando!'

@candidate_bp.route('/getAllCandidates', methods=['GET'])
def obter_dados():
    dados = candidate_service.obter_dados()
    dados_flask = dados.to_dict(orient='records')
    return jsonify(dados_flask)

@candidate_bp.route('/getCandidateFromParty', methods=['GET'])
def get_candidate_from_party():
    user_party = request.args.get('party')

    if not user_party:
        return jsonify({"error": "Nome do partido é necessário."}), 400

    dados = candidate_service.get_from_party(user_party)
    return jsonify(dados)




