from app.models.curriculo import Curriculo


class CurriculoService:
    @staticmethod
    def criar_curriculo(dados):
        if not dados.get("usuario_id") or not dados.get("nome_arquivo"):
            raise ValueError("Campos 'usuario_id' e 'nome_arquivo' são obrigatórios.")
        return Curriculo.criar(
            usuario_id=dados["usuario_id"],
            nome_arquivo=dados["nome_arquivo"],
            conteudo_texto=dados.get("conteudo_texto"),
            pontos_fortes=dados.get("pontos_fortes"),
            pontos_a_melhorar=dados.get("pontos_a_melhorar"),
        )

    @staticmethod
    def listar_curriculos():
        return Curriculo.listar()

    @staticmethod
    def buscar_curriculo(curriculo_id):
        curriculo = Curriculo.buscar_por_id(curriculo_id)
        if not curriculo:
            raise LookupError("Currículo não encontrado.")
        return curriculo

    @staticmethod
    def atualizar_curriculo(curriculo_id, dados):
        curriculo = CurriculoService.buscar_curriculo(curriculo_id)
        return curriculo.atualizar(
            nome_arquivo=dados.get("nome_arquivo"),
            conteudo_texto=dados.get("conteudo_texto"),
            pontos_fortes=dados.get("pontos_fortes"),
            pontos_a_melhorar=dados.get("pontos_a_melhorar"),
        )

    @staticmethod
    def deletar_curriculo(curriculo_id):
        curriculo = CurriculoService.buscar_curriculo(curriculo_id)
        curriculo.deletar()
