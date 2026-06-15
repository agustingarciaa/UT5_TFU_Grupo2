from app.domain.pedido import Pedido


class PedidoRepository:
    """Persistencia de Pedidos (en memoria por ahora)."""

    _pedidos = {}      # id -> Pedido
    _next_id = 1

    def obtener_pedido_x_id(self, pedido_id) -> Pedido:
        return self._pedidos.get(int(pedido_id))

    def crear_pedido(self) -> Pedido:
        pedido = Pedido(id=PedidoRepository._next_id)
        self._pedidos[pedido.id] = pedido
        PedidoRepository._next_id += 1
        return pedido

    def borrar_pedido(self, pedido_id) -> None:
        self._pedidos.pop(int(pedido_id), None)

    def listar(self) -> list:
        return list(self._pedidos.values())
