from app.domain.enums import EstadoP, Pago


class Pedido:
    def __init__(self, id: int, monto: float = 0.0,
                 estado: EstadoP = EstadoP.EN_PREPARACION,
                 metodo_pago: Pago = None):
        self.id = id
        self.monto = monto
        self.estado = estado
        self.metodo_pago = metodo_pago
        self.productos = []   # List[ArticuloPedido]

    def add_producto(self, articulo_pedido) -> None:
        self.productos.append(articulo_pedido)

    def get_productos(self) -> list:
        return self.productos

    def remover_producto(self, id_articulo_pedido) -> None:
        self.productos = [ap for ap in self.productos
                          if ap.id != id_articulo_pedido]
