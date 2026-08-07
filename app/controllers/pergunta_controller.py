from flask import Blueprint, jsonify, request, render_template

from app.services.pergunta_service import PerguntaService

pergunta_bp = Blueprint("pergunta_bp", __name__)


@pergunta_bp.route("/perguntas")
def tela_perguntas():
    return render_template("perguntas/list.html", active="perguntas")


@pergunta_bp.route("/api/perguntas", methods=["GET"])
def listar_perguntas():
    perguntas = PerguntaService.listar_perguntas()
    return jsonify([p.to_dict() for p in perguntas])


@pergunta_bp.route("/api/perguntas/<int:pergunta_id>", methods=["GET"])
def buscar_pergunta(pergunta_id):
    try:
        pergunta = PerguntaService.buscar_pergunta(pergunta_id)
        return jsonify(pergunta.to_dict())
    except LookupError as e:
        return jsonify({"erro": str(e)}), 404


@pergunta_bp.route("/api/perguntas", methods=["POST"])
def criar_pergunta():
    try:
        pergunta = PerguntaService.criar_pergunta(request.get_json(force=True))
        return jsonify(pergunta.to_dict()), 201
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400


@pergunta_bp.route("/api/perguntas/<int:pergunta_id>", methods=["PUT"])
def atualizar_pergunta(pergunta_id):
    try:
        pergunta = PerguntaService.atualizar_pergunta(pergunta_id, request.get_json(force=True))
        return jsonify(pergunta.to_dict())
    except LookupError as e:
        return jsonify({"erro": str(e)}), 404
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400


@pergunta_bp.route("/api/perguntas/<int:pergunta_id>", methods=["DELETE"])
def deletar_pergunta(pergunta_id):
    try:
        PerguntaService.deletar_pergunta(pergunta_id)
        return jsonify({"mensagem": "Pergunta excluída com sucesso."})
    except LookupError as e:
        return jsonify({"erro": str(e)}), 404
