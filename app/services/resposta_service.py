from app.models.resposta import Resposta


class RespostaService:
    @staticmethod
    def criar_resposta(dados):
        obrigatorios = ("entrevista_id", "pergunta_id", "texto_resposta")
        if not all(dados.get(campo) for campo in obrigatorios):
            raise ValueError("Campos 'entrevista_id', 'pergunta_id' e 'texto_resposta' são obrigatórios.")
        return Resposta.criar(
            entrevista_id=dados["entrevista_id"],
            pergunta_id=dados["pergunta_id"],
            texto_resposta=dados["texto_resposta"],
            tipo=dados.get("tipo", "texto"),
        )

    @staticmethod
    def listar_respostas():
        return Resposta.listar()

    @staticmethod
    def buscar_resposta(resposta_id):
        resposta = Resposta.buscar_por_id(resposta_id)
        if not resposta:
            raise LookupError("Resposta não encontrada.")
        return resposta

    @staticmethod
    def atualizar_resposta(resposta_id, dados):
        resposta = RespostaService.buscar_resposta(resposta_id)
        return resposta.atualizar(
            texto_resposta=dados.get("texto_resposta"),
            tipo=dados.get("tipo"),
        )

    @staticmethod
    def deletar_resposta(resposta_id):
        resposta = RespostaService.buscar_resposta(resposta_id)
        resposta.deletar()
