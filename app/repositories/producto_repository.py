from app.extensions import db
from app.domain.producto import Producto


class ProductoRepository:
    """Catalogo de productos contra la base de datos."""

    def obtener_producto_x_id(self, producto_id) -> Producto:
        return db.session.get(Producto, int(producto_id))

    def obtener_productos_x_categoria(self, categoria: str = None) -> list:
        query = Producto.query
        if categoria:
            query = query.filter_by(categoria=categoria)
        return query.all()

    def obtener_categorias(self) -> list:
        filas = db.session.query(Producto.categoria).distinct().all()
        return sorted(c[0] for c in filas if c[0])
