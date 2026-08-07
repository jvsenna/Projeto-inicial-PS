from datetime import datetime
from app.extensions import db


class Curriculo(db.Model):
    """Model da entidade Currículo (upload e análise de currículo)."""

    __tablename__ = "curriculos"

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=False)
    nome_arquivo = db.Column(db.String(255), nullable=False)
    conteudo_texto = db.Column(db.Text, nullable=True)
    pontos_fortes = db.Column(db.Text, nullable=True)
    pontos_a_melhorar = db.Column(db.Text, nullable=True)
    enviado_em = db.Column(db.DateTime, default=datetime.utcnow)

    # ---------- CRUD ----------
    @classmethod
    def criar(cls, usuario_id, nome_arquivo, conteudo_texto=None,
              pontos_fortes=None, pontos_a_melhorar=None):
        curriculo = cls(
            usuario_id=usuario_id,
            nome_arquivo=nome_arquivo,
            conteudo_texto=conteudo_texto,
            pontos_fortes=pontos_fortes,
            pontos_a_melhorar=pontos_a_melhorar,
        )
        db.session.add(curriculo)
        db.session.commit()
        return curriculo

    @classmethod
    def listar(cls):
        return cls.query.order_by(cls.id).all()

    @classmethod
    def buscar_por_id(cls, curriculo_id):
        return cls.query.get(curriculo_id)

    def atualizar(self, nome_arquivo=None, conteudo_texto=None,
                  pontos_fortes=None, pontos_a_melhorar=None):
        if nome_arquivo is not None:
            self.nome_arquivo = nome_arquivo
        if conteudo_texto is not None:
            self.conteudo_texto = conteudo_texto
        if pontos_fortes is not None:
            self.pontos_fortes = pontos_fortes
        if pontos_a_melhorar is not None:
            self.pontos_a_melhorar = pontos_a_melhorar
        db.session.commit()
        return self

    def deletar(self):
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "nome_arquivo": self.nome_arquivo,
            "conteudo_texto": self.conteudo_texto,
            "pontos_fortes": self.pontos_fortes,
            "pontos_a_melhorar": self.pontos_a_melhorar,
            "enviado_em": self.enviado_em.isoformat() if self.enviado_em else None,
        }
