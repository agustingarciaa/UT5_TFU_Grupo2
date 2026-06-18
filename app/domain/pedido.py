from app.extensions import db
from app.domain.enums import EstadoP, Pago


class Pedido(db.Model):
    __tablename__ = "pedidos"

    id = db.Column(db.Integer, primary_key=True)
    monto = db.Column(db.Float, nullable=False, default=0.0)
    estado = db.Column(db.Enum(EstadoP), default=EstadoP.EN_PREPARACION, nullable=False)
    metodo_pago = db.Column(db.Enum(Pago), nullable=True)

    productos = db.relationship(
        "ArticuloPedido", backref="pedido",
        cascade="all, delete-orphan", lazy="select",
    )

    def add_producto(self, articulo_pedido) -> None:
        self.productos.append(articulo_pedido)

    def get_productos(self) -> list:
        return self.productos

    def remover_producto(self, id_articulo_pedido) -> None:
        self.productos = [ap for ap in self.productos
                          if ap.id != int(id_articulo_pedido)]

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "monto": self.monto,
            "estado": self.estado.value if self.estado else None,
            "metodo_pago": self.metodo_pago.value if self.metodo_pago else None,
            "productos": [ap.to_dict() for ap in self.productos],
        }
