from app.extensions import db
from app.domain.pedido import Pedido


class PedidoRepository:
    """Persistencia de Pedidos contra la base de datos."""

    def obtener_pedido_x_id(self, pedido_id) -> Pedido:
        return db.session.get(Pedido, int(pedido_id))

    def crear_pedido(self) -> Pedido:
        pedido = Pedido()
        db.session.add(pedido)
        db.session.commit()
        return pedido

    def borrar_pedido(self, pedido_id) -> bool:
        pedido = self.obtener_pedido_x_id(pedido_id)
        if not pedido:
            return False
        db.session.delete(pedido)
        db.session.commit()
        return True

    def guardar(self) -> None:
        db.session.commit()

    def listar(self) -> list:
        return Pedido.query.all()
