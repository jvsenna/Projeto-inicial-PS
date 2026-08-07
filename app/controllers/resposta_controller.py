from flask import Blueprint, jsonify, request, render_template

from app.services.resposta_service import RespostaService

resposta_bp = Blueprint("resposta_bp", __name__)


@resposta_bp.route("/respostas")
def tela_respostas():
    return render_template("respostas/list.html", active="respostas")


@resposta_bp.route("/api/respostas", methods=["GET"])
def listar_respostas():
    respostas = RespostaService.listar_respostas()
    return jsonify([r.to_dict() for r in respostas])


@resposta_bp.route("/api/respostas/<int:resposta_id>", methods=["GET"])
def buscar_resposta(resposta_id):
    try:
        resposta = RespostaService.buscar_resposta(resposta_id)
        return jsonify(resposta.to_dict())
    except LookupError as e:
        return jsonify({"erro": str(e)}), 404


@resposta_bp.route("/api/respostas", methods=["POST"])
def criar_resposta():
    try:
        resposta = RespostaService.criar_resposta(request.get_json(force=True))
        return jsonify(resposta.to_dict()), 201
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400


@resposta_bp.route("/api/respostas/<int:resposta_id>", methods=["PUT"])
def atualizar_resposta(resposta_id):
    try:
        resposta = RespostaService.atualizar_resposta(resposta_id, request.get_json(force=True))
        return jsonify(resposta.to_dict())
    except LookupError as e:
        return jsonify({"erro": str(e)}), 404
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400


@resposta_bp.route("/api/respostas/<int:resposta_id>", methods=["DELETE"])
def deletar_resposta(resposta_id):
    try:
        RespostaService.deletar_resposta(resposta_id)
        return jsonify({"mensagem": "Resposta excluída com sucesso."})
    except LookupError as e:
        return jsonify({"erro": str(e)}), 404
