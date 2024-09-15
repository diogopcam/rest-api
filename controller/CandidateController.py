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

@candidate_bp.route('/getCandidateByNumber', methods=['GET'])
def get_candidate_by_number():
    candidate_number = request.args.get('candidateNumber')

    if not candidate_number:
        return jsonify({"error": "Número do candidato é necessário."}), 400

    candidate = candidate_service.get_by_number(candidate_number)
    return jsonify(candidate)

@candidate_bp.route('/addCandidate', methods=['PUT'])
def add_candidate():
    data = request.get_json()

    required_fields = [
        "CD_CARGO", "DS_CARGO", "DS_COR_RACA", "DS_EMAIL", "DS_ESTADO_CIVIL",
        "DS_GENERO", "DS_GRAU_INSTRUCAO", "DS_OCUPACAO", "DT_NASCIMENTO",
        "NM_CANDIDATO", "NM_PARTIDO", "NM_SOCIAL_CANDIDATO", "NM_URNA_CANDIDATO",
        "NR_CANDIDATO", "NR_PARTIDO", "NR_TITULO_ELEITORAL_CANDIDATO", "SG_PARTIDO",
        "SG_UF_NASCIMENTO"
    ]

    if not data:
        return jsonify({"error": "Dados do candidato são necessários."}), 400

    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return jsonify({"error": f"Campos obrigatórios ausentes: {', '.join(missing_fields)}"}), 400

    candidate_service.add_candidate(data)
    return jsonify({"message": "Candidato adicionado com sucesso."})

@candidate_bp.route('/updateCandidate', methods=['PATCH'])
def update_candidate():
    candidate_number = request.args.get('candidateNumber')
    data = request.get_json()

    if not candidate_number:
        return jsonify({"error": "Número do candidato é necessário."}), 400
    
    if not data:
        return jsonify({"error": "Dados do candidato são necessários."}), 400
    
    candidate_service.update_candidate(candidate_number, data)
    return jsonify({"message": "Candidato atualizado com sucesso."})

@candidate_bp.route('/deleteCandidate', methods=['DELETE'])
def delete_candidate():
    candidate_number = request.args.get('candidateNumber')

    if not candidate_number:
        return jsonify({"error": "Número do candidato é necessário."}), 400

    candidate_service.delete_candidate(candidate_number)
    return jsonify({"message": "Candidato deletado com sucesso."})


