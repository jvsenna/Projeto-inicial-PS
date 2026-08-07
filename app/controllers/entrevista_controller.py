from flask import Blueprint, jsonify, request, render_template

from app.services.entrevista_service import EntrevistaService

entrevista_bp = Blueprint("entrevista_bp", __name__)


@entrevista_bp.route("/entrevistas")
def tela_entrevistas():
    return render_template("entrevistas/list.html", active="entrevistas")


@entrevista_bp.route("/api/entrevistas", methods=["GET"])
def listar_entrevistas():
    entrevistas = EntrevistaService.listar_entrevistas()
    return jsonify([e.to_dict() for e in entrevistas])


@entrevista_bp.route("/api/entrevistas/<int:entrevista_id>", methods=["GET"])
def buscar_entrevista(entrevista_id):
    try:
        entrevista = EntrevistaService.buscar_entrevista(entrevista_id)
        return jsonify(entrevista.to_dict())
    except LookupError as e:
        return jsonify({"erro": str(e)}), 404


@entrevista_bp.route("/api/entrevistas", methods=["POST"])
def criar_entrevista():
    try:
        entrevista = EntrevistaService.criar_entrevista(request.get_json(force=True))
        return jsonify(entrevista.to_dict()), 201
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400


@entrevista_bp.route("/api/entrevistas/<int:entrevista_id>", methods=["PUT"])
def atualizar_entrevista(entrevista_id):
    try:
        entrevista = EntrevistaService.atualizar_entrevista(entrevista_id, request.get_json(force=True))
        return jsonify(entrevista.to_dict())
    except LookupError as e:
        return jsonify({"erro": str(e)}), 404
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400


@entrevista_bp.route("/api/entrevistas/<int:entrevista_id>", methods=["DELETE"])
def deletar_entrevista(entrevista_id):
    try:
        EntrevistaService.deletar_entrevista(entrevista_id)
        return jsonify({"mensagem": "Entrevista excluída com sucesso."})
    except LookupError as e:
        return jsonify({"erro": str(e)}), 404
