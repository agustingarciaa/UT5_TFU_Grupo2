class ArticuloPedido:
    """Linea de un pedido: referencia a un Producto + datos propios (aclaracion)."""

    def __init__(self, id: int, producto, aclaracion: str = ""):
        self.id = id
        self.producto = producto          # asociacion 1 -> Producto
        self.aclaracion = aclaracion
