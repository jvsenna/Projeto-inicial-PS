from app.models.entrevista import Entrevista


class EntrevistaService:
    @staticmethod
    def criar_entrevista(dados):
        if not dados.get("usuario_id"):
            raise ValueError("O campo 'usuario_id' é obrigatório.")
        return Entrevista.criar(
            usuario_id=dados["usuario_id"],
            tipo=dados.get("tipo", "texto"),
            status=dados.get("status", "em_andamento"),
            pontuacao_geral=dados.get("pontuacao_geral"),
        )

    @staticmethod
    def listar_entrevistas():
        return Entrevista.listar()

    @staticmethod
    def buscar_entrevista(entrevista_id):
        entrevista = Entrevista.buscar_por_id(entrevista_id)
        if not entrevista:
            raise LookupError("Entrevista não encontrada.")
        return entrevista

    @staticmethod
    def atualizar_entrevista(entrevista_id, dados):
        entrevista = EntrevistaService.buscar_entrevista(entrevista_id)
        return entrevista.atualizar(
            tipo=dados.get("tipo"),
            status=dados.get("status"),
            pontuacao_geral=dados.get("pontuacao_geral"),
        )

    @staticmethod
    def deletar_entrevista(entrevista_id):
        entrevista = EntrevistaService.buscar_entrevista(entrevista_id)
        entrevista.deletar()
