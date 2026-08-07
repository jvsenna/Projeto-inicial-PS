from app.models.usuario import Usuario


class UsuarioService:
    """Camada de serviço: valida dados e orquestra chamadas ao Model Usuario."""

    @staticmethod
    def criar_usuario(dados):
        if not dados.get("nome") or not dados.get("email") or not dados.get("senha"):
            raise ValueError("Campos 'nome', 'email' e 'senha' são obrigatórios.")
        return Usuario.criar(dados["nome"], dados["email"], dados["senha"])

    @staticmethod
    def listar_usuarios():
        return Usuario.listar()

    @staticmethod
    def buscar_usuario(usuario_id):
        usuario = Usuario.buscar_por_id(usuario_id)
        if not usuario:
            raise LookupError("Usuário não encontrado.")
        return usuario

    @staticmethod
    def atualizar_usuario(usuario_id, dados):
        usuario = UsuarioService.buscar_usuario(usuario_id)
        return usuario.atualizar(
            nome=dados.get("nome"),
            email=dados.get("email"),
            senha=dados.get("senha"),
        )

    @staticmethod
    def deletar_usuario(usuario_id):
        usuario = UsuarioService.buscar_usuario(usuario_id)
        usuario.deletar()
