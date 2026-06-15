from flask import Flask, redirect, url_for


def create_app():
    app = Flask(__name__)

    from app.controllers.crear_pedido_controller import bp as pedidos_bp
    from app.controllers.estados_controller import bp as estados_bp

    app.register_blueprint(pedidos_bp)
    app.register_blueprint(estados_bp)

    @app.route("/")
    def index():
        return redirect(url_for("pedidos.inicio"))

    return app
