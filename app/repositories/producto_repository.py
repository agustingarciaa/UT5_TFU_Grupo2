from app.domain.producto import Producto


class ProductoRepository:
    """Catalogo de productos (datos de ejemplo en memoria)."""

    _productos = {
        1: Producto(1, "Pizza Muzzarella", 8500.0, "Pizzas",
                    ["Muzzarella", "Salsa de tomate", "Oregano"]),
        2: Producto(2, "Empanada de carne", 1200.0, "Empanadas",
                    ["Carne", "Cebolla", "Huevo"]),
        3: Producto(3, "Coca-Cola 500ml", 1500.0, "Bebidas", []),
    }

    def obtener_producto_x_id(self, producto_id) -> Producto:
        return self._productos.get(int(producto_id))

    def obtener_productos_x_categoria(self, categoria: str = None) -> list:
        productos = list(self._productos.values())
        if categoria:
            productos = [p for p in productos if p.categoria == categoria]
        return productos

    def obtener_categorias(self) -> list:
        return sorted({p.categoria for p in self._productos.values() if p.categoria})
