from flask import Blueprint, jsonify, request, render_template

from app.services.curriculo_service import CurriculoService

curriculo_bp = Blueprint("curriculo_bp", __name__)


@curriculo_bp.route("/curriculos")
def tela_curriculos():
    return render_template("curriculos/list.html", active="curriculos")


@curriculo_bp.route("/api/curriculos", methods=["GET"])
def listar_curriculos():
    curriculos = CurriculoService.listar_curriculos()
    return jsonify([c.to_dict() for c in curriculos])


@curriculo_bp.route("/api/curriculos/<int:curriculo_id>", methods=["GET"])
def buscar_curriculo(curriculo_id):
    try:
        curriculo = CurriculoService.buscar_curriculo(curriculo_id)
        return jsonify(curriculo.to_dict())
    except LookupError as e:
        return jsonify({"erro": str(e)}), 404


@curriculo_bp.route("/api/curriculos", methods=["POST"])
def criar_curriculo():
    try:
        curriculo = CurriculoService.criar_curriculo(request.get_json(force=True))
        return jsonify(curriculo.to_dict()), 201
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400


@curriculo_bp.route("/api/curriculos/<int:curriculo_id>", methods=["PUT"])
def atualizar_curriculo(curriculo_id):
    try:
        curriculo = CurriculoService.atualizar_curriculo(curriculo_id, request.get_json(force=True))
        return jsonify(curriculo.to_dict())
    except LookupError as e:
        return jsonify({"erro": str(e)}), 404
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400


@curriculo_bp.route("/api/curriculos/<int:curriculo_id>", methods=["DELETE"])
def deletar_curriculo(curriculo_id):
    try:
        CurriculoService.deletar_curriculo(curriculo_id)
        return jsonify({"mensagem": "Currículo excluído com sucesso."})
    except LookupError as e:
        return jsonify({"erro": str(e)}), 404
