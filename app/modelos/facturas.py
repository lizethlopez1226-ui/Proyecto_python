from pydantic import BaseModel, computed_field
from .transacciones import Transaccion
from.clientes  import Cliente
from datetime import datetime

class FacturaBase(BaseModel):
    fecha: str = datetime .now ()
    cliente: Cliente
    transsacciones: list [Transaccion] = []


    @computed_field
    @property
    def vr_total(self) -> float:
        #calcular cantidad *vr unitario
        #consultar id actual de la factura
        factura_id_actual = getattr(self,"id", None)
        total_factura = 0.0
        if not factura_id_actual or not self.transsacciones:
            return 0.0
        #recorrer la lista de transacciones segun el factura id
        for transaccion in self.transsacciones:
            if transaccion.factura_id == factura_id_actual:
                total_factura += transaccion.vr_unitario * transaccion.cantidad
        return total_factura

class FacturaCrear(FacturaBase):
    pass

class FacturaEditar(FacturaBase):
    pass

class Factura(FacturaBase):
    id: int | None = None