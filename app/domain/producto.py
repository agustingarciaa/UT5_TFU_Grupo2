from app.extensions import db


class Producto(db.Model):
    __tablename__ = "productos"

    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(120), nullable=False)
    precio_unitario = db.Column(db.Float, nullable=False, default=0.0)
    categoria = db.Column(db.String(60))

    ingredientes = db.relationship(
        "Ingrediente", backref="producto",
        cascade="all, delete-orphan", lazy="select",
    )

    def get_descripcion(self) -> str:
        return self.descripcion

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "descripcion": self.descripcion,
            "precio_unitario": self.precio_unitario,
            "categoria": self.categoria,
            "ingredientes": [i.nombre for i in self.ingredientes],
        }
