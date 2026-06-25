from fastapi import FastAPI, HTTPException, status

from app.modelos.clientes import Cliente, ClienteCrear, ClienteEditar
from app.modelos.facturas import Factura, FacturaCrear, FacturaEditar
from app.modelos.transacciones import Transaccion,TransaccionCrear,TransaccionEditar

from app.enrutadores import clientes
from app.enrutadores import facturas
from app.enrutadores import transacciones

app = FastAPI()

lista_clientes: list[Cliente] = []
lista_facturas: list[Factura] = []
lista_transacciones: list[Transaccion] = []

# Incluir rutas
app.include_router(clientes.rutas_clientes,tags=["Clientes"])
app.include_router(facturas.rutas_facturas,tags=["Facturas"])
app.include_router(transacciones.rutas_transacciones,tags=["Transacciones"])