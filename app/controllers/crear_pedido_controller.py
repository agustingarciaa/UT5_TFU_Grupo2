from flask import Blueprint, render_template, request, redirect, url_for

from app.services.pedido_service import PedidoService
from app.repositories.producto_repository import ProductoRepository
from app.domain.enums import Pago

bp = Blueprint("pedidos", __name__, url_prefix="/pedidos")

service = PedidoService()
producto_repo = ProductoRepository()


# IniciarPedidoView -> RedirigirListaProductos()
@bp.route("/iniciar", methods=["POST"])
def registrar_pedido():
    pedido = service.registrar_pedido()
    return redirect(url_for("pedidos.listar_productos", pedido_id=pedido.id))


# ListarProductosView -> MostrarProductos() / MostrarCategorias()
@bp.route("/<int:pedido_id>/productos")
def listar_productos(pedido_id):
    categoria = request.args.get("categoria")
    productos = producto_repo.obtener_productos_x_categoria(categoria)
    categorias = producto_repo.obtener_categorias()
    return render_template(
        "listar_productos.html",
        pedido_id=pedido_id,
        productos=productos,
        categorias=categorias,
    )


# DetalleProductoView -> MostrarIngredientes() / MostrarBotonAgregar()
@bp.route("/<int:pedido_id>/producto/<int:producto_id>")
def detalle_producto(pedido_id, producto_id):
    producto = producto_repo.obtener_producto_x_id(producto_id)
    return render_template(
        "detalle_producto.html", pedido_id=pedido_id, producto=producto
    )


@bp.route("/<int:pedido_id>/agregar/<int:producto_id>", methods=["POST"])
def agregar_producto(pedido_id, producto_id):
    aclaracion = request.form.get("aclaracion", "")
    service.agregar_producto(pedido_id, producto_id, aclaracion)
    return redirect(url_for("pedidos.detalle_pedido", pedido_id=pedido_id))


# DetallePedidoView -> MostrarProductosPedido() / MostrarBotonEliminar()
@bp.route("/<int:pedido_id>")
def detalle_pedido(pedido_id):
    pedido = service.obtener_pedido(pedido_id)
    articulos = service.obtener_productos_pedido(pedido_id)
    return render_template(
        "detalle_pedido.html", pedido=pedido, articulos=articulos
    )


@bp.route("/<int:pedido_id>/eliminar/<int:articulo_id>", methods=["POST"])
def eliminar_producto(pedido_id, articulo_id):
    service.eliminar_producto(articulo_id, pedido_id)
    return redirect(url_for("pedidos.detalle_pedido", pedido_id=pedido_id))


@bp.route("/<int:pedido_id>/editar/<int:articulo_id>", methods=["POST"])
def editar_producto_pedido(pedido_id, articulo_id):
    aclaracion = request.form.get("aclaracion", "")
    service.editar_producto_pedido(pedido_id, articulo_id, aclaracion)
    return redirect(url_for("pedidos.detalle_pedido", pedido_id=pedido_id))


@bp.route("/<int:pedido_id>/cancelar", methods=["POST"])
def cancelar_pedido(pedido_id):
    service.cancelar_pedido(pedido_id)
    return redirect(url_for("pedidos.inicio"))


@bp.route("/<int:pedido_id>/pago", methods=["POST"])
def seleccionar_metodo_pago(pedido_id):
    metodo = Pago(request.form["metodo_pago"])
    service.seleccionar_metodo_pago(pedido_id, metodo)
    return redirect(url_for("pedidos.detalle_pedido", pedido_id=pedido_id))


@bp.route("/")
def inicio():
    return render_template("iniciar_pedido.html")
