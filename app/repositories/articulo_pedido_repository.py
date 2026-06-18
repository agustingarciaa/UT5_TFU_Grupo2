from app.extensions import db
from app.domain.articulo_pedido import ArticuloPedido


class ArticuloPedidoRepository:
    """Persistencia de los articulos (lineas) de un pedido."""

    def agregar_articulo_pedido(self, articulo: ArticuloPedido) -> ArticuloPedido:
        db.session.add(articulo)
        db.session.commit()
        return articulo

    def buscar_x_id(self, id_articulo) -> ArticuloPedido:
        return db.session.get(ArticuloPedido, int(id_articulo))

    def editar_aclaracion(self, id_articulo, aclaracion: str) -> ArticuloPedido:
        articulo = self.buscar_x_id(id_articulo)
        if articulo:
            articulo.aclaracion = aclaracion
            db.session.commit()
        return articulo

    def borrar_articulo_pedido(self, id_articulo) -> bool:
        articulo = self.buscar_x_id(id_articulo)
        if not articulo:
            return False
        db.session.delete(articulo)
        db.session.commit()
        return True

    def get_articulos_x_pedido(self, id_pedido) -> list:
        return ArticuloPedido.query.filter_by(pedido_id=int(id_pedido)).all()
