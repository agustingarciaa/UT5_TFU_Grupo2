from enum import Enum


class EstadoP(Enum):
    EN_PREPARACION = "EnPreparacion"
    LISTO = "Listo"
    ENTREGADO = "Entregado"


class Pago(Enum):
    MERCADO_PAGO = "MercadoPago"
    TARJETA = "Tarjeta"
    EFECTIVO = "Efectivo"
