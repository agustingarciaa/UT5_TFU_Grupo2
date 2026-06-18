from flask import Blueprint, jsonify, request

from app.controllers.crear_pedido_controller import CrearPedidoController
from app.controllers.estados_controller import ControlarEstados

bp = Blueprint("pedidos", __name__, url_prefix="/pedidos")
controller = CrearPedidoController()
estados_controller = ControlarEstados()


# ===== PUC2: estados =====

# GET /pedidos/estados  -> estados posibles (antes que /<id>)
@bp.get("/estados")
def obtener_estados():
    return jsonify(estados_controller.obtener_estados())


# POST /pedidos/:id?estado=  -> actualizar el estado del pedido
@bp.post("/<int:pedido_id>")
def actualizar_estado(pedido_id):
    estado = request.args.get("estado") or (request.json or {}).get("estado")
    if not estado:
        return jsonify({"error": "Falta el parametro 'estado'"}), 400
    try:
        pedido = estados_controller.actualizar_estado(pedido_id, estado)
    except ValueError:
        return jsonify({"error": f"Estado invalido: {estado}"}), 400
    if pedido is None:
        return jsonify({"error": "Pedido no encontrado"}), 404
    return jsonify(pedido)


# ===== PUC1: pedidos =====

# POST /pedidos  -> crear un pedido vacio
@bp.post("")
@bp.post("/")
def crear_pedido():
    return jsonify(controller.registrar_pedido()), 201


# GET /pedidos/:id  -> obtener un pedido
@bp.get("/<int:pedido_id>")
def obtener_pedido(pedido_id):
    pedido = controller.obtener_pedido(pedido_id)
    if pedido is None:
        return jsonify({"error": "Pedido no encontrado"}), 404
    return jsonify(pedido)


# DELETE /pedidos/:id  -> eliminar pedido
@bp.delete("/<int:pedido_id>")
def eliminar_pedido(pedido_id):
    if not controller.cancelar_pedido(pedido_id):
        return jsonify({"error": "Pedido no encontrado"}), 404
    return "", 204


# POST /pedidos/:id/productos  -> agregar un producto al pedido
@bp.post("/<int:pedido_id>/productos")
def agregar_producto(pedido_id):
    datos = request.get_json(silent=True) or {}
    producto_id = datos.get("producto_id")
    aclaracion = datos.get("aclaracion", "")
    if producto_id is None:
        return jsonify({"error": "Falta 'producto_id'"}), 400
    articulo = controller.agregar_producto(pedido_id, producto_id, aclaracion)
    if articulo is None:
        return jsonify({"error": "Pedido o producto no encontrado"}), 404
    return jsonify(articulo), 201


# GET /pedidos/:id/productos/:id  -> un articulo (producto del pedido)
@bp.get("/<int:pedido_id>/productos/<int:articulo_id>")
def obtener_producto_pedido(pedido_id, articulo_id):
    articulo = controller.obtener_producto_pedido(pedido_id, articulo_id)
    if articulo is None:
        return jsonify({"error": "Articulo no encontrado en ese pedido"}), 404
    return jsonify(articulo)


# PATCH /pedidos/:id/productos/:id  -> editar aclaracion de un articulo
@bp.patch("/<int:pedido_id>/productos/<int:articulo_id>")
def editar_producto_pedido(pedido_id, articulo_id):
    datos = request.get_json(silent=True) or {}
    aclaracion = datos.get("aclaracion", "")
    articulo = controller.editar_producto_pedido(pedido_id, articulo_id, aclaracion)
    if articulo is None:
        return jsonify({"error": "Articulo no encontrado en ese pedido"}), 404
    return jsonify(articulo)


# DELETE /pedidos/:id/productos/:id  -> eliminar un articulo del pedido
@bp.delete("/<int:pedido_id>/productos/<int:articulo_id>")
def eliminar_producto(pedido_id, articulo_id):
    if not controller.eliminar_producto(pedido_id, articulo_id):
        return jsonify({"error": "Articulo no encontrado en ese pedido"}), 404
    return "", 204
