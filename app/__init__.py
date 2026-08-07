from flask import Flask, render_template
from flask_cors import CORS

from app.extensions import db


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    db.init_app(app)
    CORS(app)

    # Importa os Models para que o SQLAlchemy os reconheça
    from app.models import usuario, curriculo, pergunta, entrevista, resposta, feedback  # noqa

    # Registra os Controllers (Blueprints) — cada um expõe rotas de API (/api/...)
    # e rotas de tela (frontend) para o respectivo Model.
    from app.controllers.usuario_controller import usuario_bp
    from app.controllers.curriculo_controller import curriculo_bp
    from app.controllers.pergunta_controller import pergunta_bp
    from app.controllers.entrevista_controller import entrevista_bp
    from app.controllers.resposta_controller import resposta_bp
    from app.controllers.feedback_controller import feedback_bp

    app.register_blueprint(usuario_bp)
    app.register_blueprint(curriculo_bp)
    app.register_blueprint(pergunta_bp)
    app.register_blueprint(entrevista_bp)
    app.register_blueprint(resposta_bp)
    app.register_blueprint(feedback_bp)

    @app.route("/")
    def index():
        return render_template("index.html", active="home")

    return app
