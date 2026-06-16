from flask import Flask

from app.config import Config
from app.extensions import db


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    # Importar modelos para que SQLAlchemy registre las tablas.
    from app.domain import producto, ingrediente, articulo_pedido, pedido  # noqa: F401

    # Registrar las rutas (endpoints).
    from app.routes.productos_routes import bp as productos_bp
    from app.routes.pedidos_routes import bp as pedidos_bp
    app.register_blueprint(productos_bp)
    app.register_blueprint(pedidos_bp)

    with app.app_context():
        db.create_all()
        _seed_si_vacio()

    return app


def _seed_si_vacio():
    """Carga productos de ejemplo si la tabla esta vacia."""
    from app.domain.producto import Producto
    from app.domain.ingrediente import Ingrediente

    if Producto.query.first():
        return

    productos = [
        Producto(descripcion="Pizza Muzzarella", precio_unitario=8500.0,
                 categoria="Pizzas",
                 ingredientes=[Ingrediente(nombre="Muzzarella"),
                               Ingrediente(nombre="Salsa de tomate"),
                               Ingrediente(nombre="Oregano")]),
        Producto(descripcion="Empanada de carne", precio_unitario=1200.0,
                 categoria="Empanadas",
                 ingredientes=[Ingrediente(nombre="Carne"),
                               Ingrediente(nombre="Cebolla"),
                               Ingrediente(nombre="Huevo")]),
        Producto(descripcion="Coca-Cola 500ml", precio_unitario=1500.0,
                 categoria="Bebidas"),
    ]
    db.session.add_all(productos)
    db.session.commit()
