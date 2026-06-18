from flask import Blueprint, jsonify, request

from app.controllers.crear_pedido_controller import CrearPedidoController

bp = Blueprint("productos", __name__, url_prefix="/productos")
controller = CrearPedidoController()


# GET /productos/categorias  -> obtener categorias
# (se define antes que /<id> para que "categorias" no matchee como id)
@bp.get("/categorias")
def obtener_categorias():
    return jsonify(controller.obtener_categorias())


# GET /productos?categoria=  -> productos (opcionalmente de una categoria)
@bp.get("")
@bp.get("/")
def listar_productos():
    categoria = request.args.get("categoria")
    return jsonify(controller.obtener_productos(categoria))


# GET /productos/:id  -> un producto con sus ingredientes
@bp.get("/<int:producto_id>")
def obtener_producto(producto_id):
    producto = controller.obtener_producto(producto_id)
    if producto is None:
        return jsonify({"error": "Producto no encontrado"}), 404
    return jsonify(producto)
