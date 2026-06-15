class Producto:
    def __init__(self, id: int, descripcion: str, precio_unitario: float,
                 categoria: str = None, ingredientes: list = None):
        self.id = id
        self.descripcion = descripcion
        self.precio_unitario = precio_unitario
        self.categoria = categoria
        self.ingredientes = ingredientes or []

    def get_descripcion(self) -> str:
        return self.descripcion
