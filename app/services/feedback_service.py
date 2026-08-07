from app.models.feedback import Feedback


class FeedbackService:
    @staticmethod
    def criar_feedback(dados):
        if not dados.get("entrevista_id") or dados.get("pontuacao") is None:
            raise ValueError("Campos 'entrevista_id' e 'pontuacao' são obrigatórios.")
        return Feedback.criar(
            entrevista_id=dados["entrevista_id"],
            pontuacao=dados["pontuacao"],
            comentario=dados.get("comentario"),
            ponto_forte=dados.get("ponto_forte"),
            ponto_a_melhorar=dados.get("ponto_a_melhorar"),
        )

    @staticmethod
    def listar_feedbacks():
        return Feedback.listar()

    @staticmethod
    def buscar_feedback(feedback_id):
        feedback = Feedback.buscar_por_id(feedback_id)
        if not feedback:
            raise LookupError("Feedback não encontrado.")
        return feedback

    @staticmethod
    def atualizar_feedback(feedback_id, dados):
        feedback = FeedbackService.buscar_feedback(feedback_id)
        return feedback.atualizar(
            pontuacao=dados.get("pontuacao"),
            comentario=dados.get("comentario"),
            ponto_forte=dados.get("ponto_forte"),
            ponto_a_melhorar=dados.get("ponto_a_melhorar"),
        )

    @staticmethod
    def deletar_feedback(feedback_id):
        feedback = FeedbackService.buscar_feedback(feedback_id)
        feedback.deletar()
