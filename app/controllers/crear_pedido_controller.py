from app.services.pedido_service import PedidoService
from app.repositories.producto_repository import ProductoRepository
from app.domain.enums import Pago


class CrearPedidoController:
    """Controller del diagrama. Cada metodo DEVUELVE datos (dict / list).
    La serializacion a JSON la hace la capa de routes."""

    def __init__(self):
        self.service = PedidoService()
        self.producto_repository = ProductoRepository()

    # --- Productos (catalogo) ---
    def obtener_producto(self, producto_id):
        producto = self.producto_repository.obtener_producto_x_id(producto_id)
        return producto.to_dict() if producto else None

    def obtener_productos(self, categoria=None):
        productos = self.producto_repository.obtener_productos_x_categoria(categoria)
        return [p.to_dict() for p in productos]

    def obtener_categorias(self):
        return self.producto_repository.obtener_categorias()

    def obtener_descripcion_producto(self, producto_id):
        producto = self.producto_repository.obtener_producto_x_id(producto_id)
        return producto.get_descripcion() if producto else None

    # --- Pedido ---
    def registrar_pedido(self):
        pedido = self.service.registrar_pedido()
        return pedido.to_dict()

    def obtener_pedido(self, pedido_id):
        pedido = self.service.obtener_pedido(pedido_id)
        return pedido.to_dict() if pedido else None

    def cancelar_pedido(self, pedido_id):
        return self.service.cancelar_pedido(pedido_id)

    def contar_productos(self, pedido_id):
        return len(self.service.obtener_productos_pedido(pedido_id))

    # --- Productos dentro del pedido ---
    def agregar_producto(self, pedido_id, producto_id, aclaracion=""):
        articulo = self.service.agregar_producto(pedido_id, producto_id, aclaracion)
        return articulo.to_dict() if articulo else None

    def obtener_productos_pedido(self, pedido_id):
        articulos = self.service.obtener_productos_pedido(pedido_id)
        return [a.to_dict() for a in articulos]

    def obtener_producto_pedido(self, pedido_id, id_articulo):
        articulo = self.service.obtener_producto_pedido(pedido_id, id_articulo)
        return articulo.to_dict() if articulo else None

    def editar_producto_pedido(self, pedido_id, id_articulo, aclaracion):
        articulo = self.service.editar_producto_pedido(pedido_id, id_articulo, aclaracion)
        return articulo.to_dict() if articulo else None

    def eliminar_producto(self, pedido_id, id_articulo):
        return self.service.eliminar_producto(pedido_id, id_articulo)

    def seleccionar_metodo_pago(self, pedido_id, metodo_pago: str):
        pedido = self.service.seleccionar_metodo_pago(pedido_id, Pago(metodo_pago))
        return pedido.to_dict() if pedido else None
