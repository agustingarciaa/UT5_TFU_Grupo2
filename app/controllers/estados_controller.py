from flask import Blueprint, render_template

from app.services.pedido_service import PedidoService
from app.domain.enums import EstadoP

bp = Blueprint("estados", __name__, url_prefix="/estados")

service = PedidoService()


# ControlarEstados -> ObtenerEstadoPedido()
# MostrarEstadosPedidoView -> MostrarEstados()
@bp.route("/<int:pedido_id>")
def mostrar_estados(pedido_id):
    estado = service.obtener_estado_pedido(pedido_id)
    return render_template(
        "estados_pedido.html",
        pedido_id=pedido_id,
        estado=estado,
        estados=list(EstadoP),
    )
