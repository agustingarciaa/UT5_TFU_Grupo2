from app.domain.articulo_pedido import ArticuloPedido
from app.domain.enums import EstadoP, Pago
from app.repositories.pedido_repository import PedidoRepository
from app.repositories.articulo_pedido_repository import ArticuloPedidoRepository
from app.repositories.producto_repository import ProductoRepository


class PedidoService:
    """Logica de negocio de Pedidos. Orquesta los repositories."""

    def __init__(self):
        self.pedido_repository = PedidoRepository()
        self.articulo_repository = ArticuloPedidoRepository()
        self.producto_repository = ProductoRepository()

    # --- Pedidos ---
    def registrar_pedido(self) -> "Pedido":
        return self.pedido_repository.crear_pedido()

    def obtener_pedido(self, pedido_id):
        return self.pedido_repository.obtener_pedido_x_id(pedido_id)

    def obtener_estado_pedido(self, pedido_id) -> EstadoP:
        pedido = self.obtener_pedido(pedido_id)
        return pedido.estado if pedido else None

    def actualizar_estado(self, pedido_id, estado: EstadoP) -> None:
        pedido = self.obtener_pedido(pedido_id)
        if pedido:
            pedido.estado = estado

    def cancelar_pedido(self, pedido_id) -> None:
        self.pedido_repository.borrar_pedido(pedido_id)

    def seleccionar_metodo_pago(self, pedido_id, metodo_pago: Pago) -> None:
        pedido = self.obtener_pedido(pedido_id)
        if pedido:
            pedido.metodo_pago = metodo_pago

    # --- Productos dentro del pedido ---
    def agregar_producto(self, pedido_id, producto_id, aclaracion="") -> None:
        pedido = self.obtener_pedido(pedido_id)
        producto = self.producto_repository.obtener_producto_x_id(producto_id)
        if not pedido or not producto:
            return
        articulo = ArticuloPedido(id=None, producto=producto, aclaracion=aclaracion)
        self.articulo_repository.agregar_articulo_pedido(articulo)
        pedido.add_producto(articulo)
        self._recalcular_monto(pedido)

    def eliminar_producto(self, producto_id, pedido_id) -> None:
        pedido = self.obtener_pedido(pedido_id)
        if not pedido:
            return
        pedido.remover_producto(producto_id)
        self.articulo_repository.borrar_articulo_pedido(producto_id)
        self._recalcular_monto(pedido)

    def editar_producto_pedido(self, pedido_id, id_articulo, aclaracion) -> None:
        self.articulo_repository.editar_aclaracion(id_articulo, aclaracion)

    def obtener_productos_pedido(self, pedido_id) -> list:
        pedido = self.obtener_pedido(pedido_id)
        return pedido.get_productos() if pedido else []

    def _recalcular_monto(self, pedido) -> None:
        pedido.monto = sum(ap.producto.precio_unitario for ap in pedido.productos)
