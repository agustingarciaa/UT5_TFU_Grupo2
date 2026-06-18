from app.extensions import db


class Ingrediente(db.Model):
    __tablename__ = "ingredientes"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    producto_id = db.Column(db.Integer, db.ForeignKey("productos.id"))

    def to_dict(self) -> dict:
        return {"id": self.id, "nombre": self.nombre}
