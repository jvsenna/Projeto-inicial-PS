from datetime import datetime
from app.extensions import db


class Usuario(db.Model):
    """Model da entidade Usuário (login e cadastro)."""

    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    senha = db.Column(db.String(255), nullable=False)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)

    curriculos = db.relationship("Curriculo", backref="usuario", cascade="all, delete-orphan")
    entrevistas = db.relationship("Entrevista", backref="usuario", cascade="all, delete-orphan")

    # ---------- CRUD ----------
    @classmethod
    def criar(cls, nome, email, senha):
        usuario = cls(nome=nome, email=email, senha=senha)
        db.session.add(usuario)
        db.session.commit()
        return usuario

    @classmethod
    def listar(cls):
        return cls.query.order_by(cls.id).all()

    @classmethod
    def buscar_por_id(cls, usuario_id):
        return cls.query.get(usuario_id)

    def atualizar(self, nome=None, email=None, senha=None):
        if nome is not None:
            self.nome = nome
        if email is not None:
            self.email = email
        if senha is not None:
            self.senha = senha
        db.session.commit()
        return self

    def deletar(self):
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "criado_em": self.criado_em.isoformat() if self.criado_em else None,
        }
