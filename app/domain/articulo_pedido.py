from app.extensions import db


class ArticuloPedido(db.Model):
    """Linea de un pedido: un Producto + datos propios (aclaracion)."""

    __tablename__ = "articulos_pedido"

    id = db.Column(db.Integer, primary_key=True)
    aclaracion = db.Column(db.String(200), default="")
    pedido_id = db.Column(db.Integer, db.ForeignKey("pedidos.id"))
    producto_id = db.Column(db.Integer, db.ForeignKey("productos.id"))

    producto = db.relationship("Producto")

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "pedido_id": self.pedido_id,
            "aclaracion": self.aclaracion,
            "producto": self.producto.to_dict() if self.producto else None,
        }
