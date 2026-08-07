from app.models.pergunta import Pergunta


class PerguntaService:
    @staticmethod
    def criar_pergunta(dados):
        if not dados.get("texto"):
            raise ValueError("O campo 'texto' é obrigatório.")
        return Pergunta.criar(
            texto=dados["texto"],
            categoria=dados.get("categoria", "comportamental"),
            dificuldade=dados.get("dificuldade", "media"),
            sugestao_resposta=dados.get("sugestao_resposta"),
        )

    @staticmethod
    def listar_perguntas():
        return Pergunta.listar()

    @staticmethod
    def buscar_pergunta(pergunta_id):
        pergunta = Pergunta.buscar_por_id(pergunta_id)
        if not pergunta:
            raise LookupError("Pergunta não encontrada.")
        return pergunta

    @staticmethod
    def atualizar_pergunta(pergunta_id, dados):
        pergunta = PerguntaService.buscar_pergunta(pergunta_id)
        return pergunta.atualizar(
            texto=dados.get("texto"),
            categoria=dados.get("categoria"),
            dificuldade=dados.get("dificuldade"),
            sugestao_resposta=dados.get("sugestao_resposta"),
        )

    @staticmethod
    def deletar_pergunta(pergunta_id):
        pergunta = PerguntaService.buscar_pergunta(pergunta_id)
        pergunta.deletar()
