class ListarProductosView:
    """Vista 'Listar productos' del diagrama.
    La implementacion real la hace el front (outsourcing).
    Esta clase solo define el contrato de metodos."""

    def mostrar_productos(self):
        raise NotImplementedError

    def mostrar_categorias(self):
        raise NotImplementedError

    def mostrar_cantidad_productos(self):
        raise NotImplementedError

    def mostrar_boton_cancelar_pedido(self):
        raise NotImplementedError
