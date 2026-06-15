from app.domain.articulo_pedido import ArticuloPedido


class ArticuloPedidoRepository:
    """Persistencia de los articulos (lineas) de un pedido."""

    _articulos = {}    # id -> ArticuloPedido
    _next_id = 1

    def agregar_articulo_pedido(self, articulo: ArticuloPedido) -> ArticuloPedido:
        if articulo.id is None:
            articulo.id = ArticuloPedidoRepository._next_id
            ArticuloPedidoRepository._next_id += 1
        self._articulos[articulo.id] = articulo
        return articulo

    def buscar_x_id(self, id_articulo) -> ArticuloPedido:
        return self._articulos.get(int(id_articulo))

    def editar_aclaracion(self, id_articulo, aclaracion: str) -> None:
        articulo = self.buscar_x_id(id_articulo)
        if articulo:
            articulo.aclaracion = aclaracion

    def borrar_articulo_pedido(self, id_articulo) -> None:
        self._articulos.pop(int(id_articulo), None)

    def get_articulos_x_pedido(self, id_pedido) -> list:
        # En memoria devolvemos todos; con DB se filtraria por pedido.
        return list(self._articulos.values())
