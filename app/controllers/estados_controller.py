from app.services.pedido_service import PedidoService
from app.domain.enums import EstadoP


class ControlarEstados:
    """Controller de estados (PUC2). Los metodos devuelven datos."""

    def __init__(self):
        self.service = PedidoService()

    def obtener_estados(self):
        # Estados posibles (catalogo del enum).
        return [e.value for e in EstadoP]

    def obtener_estado_pedido(self, pedido_id):
        estado = self.service.obtener_estado_pedido(pedido_id)
        return estado.value if estado else None

    def actualizar_estado(self, pedido_id, estado: str):
        pedido = self.service.actualizar_estado(pedido_id, EstadoP(estado))
        return pedido.to_dict() if pedido else None
