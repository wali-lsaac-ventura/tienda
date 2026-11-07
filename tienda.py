from datos import cargar, guardar
from calculadora import sumar, restar, multiplicar, dividir, historial

class Cliente:
    def __init__(self, nombre, edad, telefono, direccion):
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono
        self.direccion = direccion

class Compra:
    def __init__(self, cliente, producto, cantidad, precio):
        self.cliente = cliente
        self.producto = producto
        self.cantidad = cantidad
        self.precio = precio
        self.total = cantidad * precio
    def mostrar(self):
        print("---Tu factura---")
        print(f"cliente: {self.cliente.nombre}")
        print(f"producto: {self.producto}")
        print(f"precio: {self.precio}")
        print(f"cantidad: {self.cantidad}")
        print(f"se enviara a: {self.cliente.direccion}")
        print(f"total: {self.total}")

def pedir_numero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Eso no es un numero, intenta de nuevo.")

productos = cargar()
guardar(productos)
lista_compras = []

while True:
    nombre = input("Ingresa tu nombre o escribe salir: ")
    if nombre == "salir":
        break

    usar = input("Quieres usar la calculadora? si / no: ")
    if usar == "si":
        while True:
            entrada = input("Escribe un numero o historial o salir: ")
            if entrada == "salir":
                break
            if entrada == "historial":
                for cuenta in historial:
                    print(cuenta)
                continue

            pnum = float(entrada)
            snum = float(input("Segundo numero: "))
            op = input("Operacion + - * / : ")

            if op == "+":
                resultado = sumar(pnum, snum)
            elif op == "-":
                resultado = restar(pnum, snum)
            elif op == "*":
                resultado = multiplicar(pnum, snum)
            elif op == "/":
                if snum == 0:
                    resultado = "error"
                else:
                    resultado = dividir(pnum, snum)

            print(resultado)
            historial.append(f"{pnum} {op} {snum} = {resultado}")

    edad = pedir_numero("Ingresa tu edad: ")
    telefono = pedir_numero("Ingresa tu telefono: ")
    direccion = input("Dinos tu direccion: ")
    cliente_nuevo = Cliente(nombre, edad, telefono, direccion)

    print("--- MENU ---")
    for k, v in productos.items():
        print(f"{k}. {v[0]} - {v[1]}")

    opcion = input("Elige 1, 2: ")
    producto, precio = productos[opcion]
    cantidad = pedir_numero("Cuantos?: ")

    compra_nueva = Compra(cliente_nuevo, producto, cantidad, precio)
    lista_compras.append(compra_nueva)
    print("Tu compra ha sido realizada")
    compra_nueva.mostrar()

print(f"Gracias! Hoy vendiste {len(lista_compras)} pedidos")
