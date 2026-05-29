from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Crear clase llamado MODELO
class Cliente(BaseModel):
    id: int
    nombre: str
    edad: int
    descripcion: str

class Factura(BaseModel):
    id: int
    cliente_id: int
    monto: float
    transacciones: list

class Transaccion(BaseModel):
    id: int
    factura_id: int
    cantidad:int
    monto: float
    descripcion: str

#listas
lista_clientes: list[Cliente] = []
lista_facturas: list[Factura] = []
lista_transacciones: list[Transaccion] = []

@app.get("/")
def inicio():
    return {"mensaje": "API funcionando correctamente"}

#clientes
# endpoint
@app.get("/clientes", response_model=list[Cliente])
def listar_clientes():
    return lista_clientes


# endpoint
@app.post("/clientes", response_model=Cliente)
def crear_clientes(datos_cliente: Cliente):
    cliente_val = Cliente.model_validate(datos_cliente.model_dump())
    lista_clientes.append(cliente_val)
    return cliente_val


# endpoint
@app.put("/clientes/{id}", response_model=Cliente)
def editar_clientes(id: int, datos_cliente: Cliente):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == id:
            cliente_val = Cliente.model_validate(datos_cliente.model_dump())
            lista_clientes[i] = cliente_val
    return cliente_val
                

# endpoint
@app.delete("/clientes/{id}")
def eliminar_clientes(id: int):
    global lista_clientes
    lista_clientes = [cliente for cliente in lista_clientes if cliente.id != id]
    return {"mensaje": "Cliente eliminado"}

#facturas
# endpoint
@app.get("/facturas", response_model=list[Factura])
def listar_facturas():
    return lista_facturas

# endpoint
@app.post("/facturas", response_model=Factura)
def crear_facturas(datos_factura: Factura):
    factura_val = Factura.model_validate(datos_factura.model_dump())
    lista_facturas.append(factura_val)
    return factura_val

#transacciones
# endpoint
@app.get("/transacciones", response_model=list[Transaccion])
def listar_transacciones():
    return lista_transacciones
    
# endpoint
@app.post("/transacciones", response_model=Transaccion)
def crear_transacciones(datos_transaccion: Transaccion):
    transaccion_val = Transaccion.model_validate(datos_transaccion.model_dump())
    lista_transacciones.append(transaccion_val)
    return transaccion_val  

