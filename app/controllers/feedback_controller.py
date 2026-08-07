from flask import Blueprint, jsonify, request, render_template

from app.services.feedback_service import FeedbackService

feedback_bp = Blueprint("feedback_bp", __name__)


@feedback_bp.route("/feedbacks")
def tela_feedbacks():
    return render_template("feedbacks/list.html", active="feedbacks")


@feedback_bp.route("/api/feedbacks", methods=["GET"])
def listar_feedbacks():
    feedbacks = FeedbackService.listar_feedbacks()
    return jsonify([f.to_dict() for f in feedbacks])


@feedback_bp.route("/api/feedbacks/<int:feedback_id>", methods=["GET"])
def buscar_feedback(feedback_id):
    try:
        feedback = FeedbackService.buscar_feedback(feedback_id)
        return jsonify(feedback.to_dict())
    except LookupError as e:
        return jsonify({"erro": str(e)}), 404


@feedback_bp.route("/api/feedbacks", methods=["POST"])
def criar_feedback():
    try:
        feedback = FeedbackService.criar_feedback(request.get_json(force=True))
        return jsonify(feedback.to_dict()), 201
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400


@feedback_bp.route("/api/feedbacks/<int:feedback_id>", methods=["PUT"])
def atualizar_feedback(feedback_id):
    try:
        feedback = FeedbackService.atualizar_feedback(feedback_id, request.get_json(force=True))
        return jsonify(feedback.to_dict())
    except LookupError as e:
        return jsonify({"erro": str(e)}), 404
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400


@feedback_bp.route("/api/feedbacks/<int:feedback_id>", methods=["DELETE"])
def deletar_feedback(feedback_id):
    try:
        FeedbackService.deletar_feedback(feedback_id)
        return jsonify({"mensagem": "Feedback excluído com sucesso."})
    except LookupError as e:
        return jsonify({"erro": str(e)}), 404
