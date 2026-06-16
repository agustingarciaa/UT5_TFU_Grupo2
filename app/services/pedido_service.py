from app.extensions import db
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
    def registrar_pedido(self):
        return self.pedido_repository.crear_pedido()

    def obtener_pedido(self, pedido_id):
        return self.pedido_repository.obtener_pedido_x_id(pedido_id)

    def obtener_estado_pedido(self, pedido_id):
        pedido = self.obtener_pedido(pedido_id)
        return pedido.estado if pedido else None

    def actualizar_estado(self, pedido_id, estado: EstadoP):
        pedido = self.obtener_pedido(pedido_id)
        if not pedido:
            return None
        pedido.estado = estado
        self.pedido_repository.guardar()
        return pedido

    def cancelar_pedido(self, pedido_id) -> bool:
        return self.pedido_repository.borrar_pedido(pedido_id)

    def seleccionar_metodo_pago(self, pedido_id, metodo_pago: Pago):
        pedido = self.obtener_pedido(pedido_id)
        if not pedido:
            return None
        pedido.metodo_pago = metodo_pago
        self.pedido_repository.guardar()
        return pedido

    # --- Productos dentro del pedido ---
    def agregar_producto(self, pedido_id, producto_id, aclaracion=""):
        pedido = self.obtener_pedido(pedido_id)
        producto = self.producto_repository.obtener_producto_x_id(producto_id)
        if not pedido or not producto:
            return None
        articulo = ArticuloPedido(producto=producto, aclaracion=aclaracion)
        pedido.add_producto(articulo)
        db.session.add(articulo)
        self._recalcular_monto(pedido)
        db.session.commit()
        return articulo

    def eliminar_producto(self, pedido_id, id_articulo) -> bool:
        articulo = self.articulo_repository.buscar_x_id(id_articulo)
        if not articulo or articulo.pedido_id != int(pedido_id):
            return False
        pedido = articulo.pedido
        db.session.delete(articulo)
        db.session.flush()
        self._recalcular_monto(pedido)
        db.session.commit()
        return True

    def editar_producto_pedido(self, pedido_id, id_articulo, aclaracion):
        articulo = self.articulo_repository.buscar_x_id(id_articulo)
        if not articulo or articulo.pedido_id != int(pedido_id):
            return None
        return self.articulo_repository.editar_aclaracion(id_articulo, aclaracion)

    def obtener_producto_pedido(self, pedido_id, id_articulo):
        articulo = self.articulo_repository.buscar_x_id(id_articulo)
        if not articulo or articulo.pedido_id != int(pedido_id):
            return None
        return articulo

    def obtener_productos_pedido(self, pedido_id) -> list:
        return self.articulo_repository.get_articulos_x_pedido(pedido_id)

    def _recalcular_monto(self, pedido) -> None:
        pedido.monto = sum(ap.producto.precio_unitario for ap in pedido.productos)
