from flask import Blueprint, jsonify, request, render_template

from app.services.usuario_service import UsuarioService

usuario_bp = Blueprint("usuario_bp", __name__)


# ---------- Tela (frontend) ----------
@usuario_bp.route("/usuarios")
def tela_usuarios():
    return render_template("usuarios/list.html", active="usuarios")


# ---------- API REST ----------
@usuario_bp.route("/api/usuarios", methods=["GET"])
def listar_usuarios():
    usuarios = UsuarioService.listar_usuarios()
    return jsonify([u.to_dict() for u in usuarios])


@usuario_bp.route("/api/usuarios/<int:usuario_id>", methods=["GET"])
def buscar_usuario(usuario_id):
    try:
        usuario = UsuarioService.buscar_usuario(usuario_id)
        return jsonify(usuario.to_dict())
    except LookupError as e:
        return jsonify({"erro": str(e)}), 404


@usuario_bp.route("/api/usuarios", methods=["POST"])
def criar_usuario():
    try:
        usuario = UsuarioService.criar_usuario(request.get_json(force=True))
        return jsonify(usuario.to_dict()), 201
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400


@usuario_bp.route("/api/usuarios/<int:usuario_id>", methods=["PUT"])
def atualizar_usuario(usuario_id):
    try:
        usuario = UsuarioService.atualizar_usuario(usuario_id, request.get_json(force=True))
        return jsonify(usuario.to_dict())
    except LookupError as e:
        return jsonify({"erro": str(e)}), 404
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400


@usuario_bp.route("/api/usuarios/<int:usuario_id>", methods=["DELETE"])
def deletar_usuario(usuario_id):
    try:
        UsuarioService.deletar_usuario(usuario_id)
        return jsonify({"mensagem": "Usuário excluído com sucesso."})
    except LookupError as e:
        return jsonify({"erro": str(e)}), 404
