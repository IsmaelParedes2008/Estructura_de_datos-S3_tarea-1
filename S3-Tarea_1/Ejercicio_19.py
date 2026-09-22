""" Inventario de productos
Clase Inventario que: 
(1) tenga método agregar_stock(producto, cantidad) que guarde en un diccionario; 
(2) tenga método restar_stock(producto, cantidad) que disminuya y retorne True si hay suficiente; 
(3) tenga método productos_bajo_stock(minimo) que retorne una lista de productos con cantidad < minimo.
Entrada
productos y cantidades
Proceso
guardar/actualizar diccionario, validar, filtrar
Salida
True/False, lista de productos
Ejemplo de entrada
inv = Inventario()
inv.agregar_stock("pan", 50)
inv.restar_stock("pan", 30)
inv.productos_bajo_stock(15)
Salida esperada
True
["pan"]
💡 Colecciones: diccionario como base de datos simple """

class Inventario:
    def __init__(self):
        self.control_inventario={}

    def agregar_stock(self, producto, cantidad):

        if producto in self.control_inventario:
            self.control_inventario[producto] += cantidad 
        else:
            self.control_inventario[producto] = cantidad  

    def restar_stock(self, producto, cantidad):
        if producto in self.control_inventario and self.control_inventario[producto] >= cantidad:
            self.control_inventario[producto] -= cantidad
            return True
        else:
            return False

    def productos_bajos_stock(self, minimo):
        lista_alerta = []
        
        for producto, cantida_libre in self.control_inventario.items():
            if cantida_libre < minimo:
                lista_alerta.append(producto)
                
        return lista_alerta     

resultado = Inventario()

while True:
    print("\n === GESTOR DE INVENTARIO DE PRODUCTOS ===")
    print("1. Agregar stock de un producto")
    print("2. Restar stock de un producto (Venta/Baja)")
    print("3. Ver productos con bajo stock (Alerta)")
    print("4. Ver todo el inventario de la bodega")
    print("5. Salir")

    opcion = input("Ingrese una opción del menú (1-5): ")

    match opcion:
        case "1":
            nombre = input("Ingrese el nombre del producto: ").lower()
            cantidad = int(input("Ingrese la cantidad a agregar: "))
            
            resultado.agregar_stock(nombre, cantidad)
            print(f"¡Stock de '{nombre}' actualizado con éxito!")

        case "2":
            nombre = input("Ingrese el nombre del producto a restar: ").lower()
            cantidad = int(input("Ingrese la cantidad a restar: "))
            
            if resultado.restar_stock(nombre, cantidad):
                print(f"Resultado: True (¡Retiro exitoso de {cantidad} unidades!)")
            else:
                print(f"Resultado: False (Error: No hay suficiente stock o el producto no existe).")

        case "3":
            limite = int(input("Ingrese la cantidad mínima para activar la alerta: "))
            criticos = resultado.productos_bajos_stock(limite)

            print(f"Productos con stock bajo el mínimo ({limite}): {criticos}")

        case "4":
            print(f"Inventario completo en bodega: {resultado.control_inventario}")

        case "5":
            print("=== CERRANDO EL GESTOR DE INVENTARIO ===")
            break

        case _:
            print("Opción inválida. Intente de nuevo.")

#EJERCICIO SIMILAR
"""Almacen

Clase Almacen que:

Tenga un método agregar_unidades(producto, cantidad) que guarde o aumente la cantidad de un producto en un diccionario.
Tenga un método retirar_unidades(producto, cantidad) que disminuya la cantidad disponible y retorne True si hay suficientes unidades. Si no hay suficientes o el producto no existe, debe retornar False.
Tenga un método productos_agotados(maximo) que retorne una lista con los productos cuya cantidad sea menor que el máximo indicado.
Entrada

Productos y cantidades.

Proceso

Guardar/actualizar el diccionario, validar cantidades y filtrar productos.

Salida

True/False y lista de productos."""

class Almacen:
    def __init__(self):
        self.productos = {}

    def agregar_unidades(self, producto, cantidad):
        if producto in self.productos:
            self.productos[producto] += cantidad
        else:
            self.productos[producto] = cantidad

    def retirar_unidades(self, producto, cantidad):
        if producto in self.productos and self.productos[producto] >= cantidad:
            self.productos[producto] -= cantidad
            return True
        else:
            return False

    def productos_agotados(self, maximo):
        lista = []

        for producto, cantidad in self.productos.items():
            if cantidad < maximo:
                lista.append(producto)

        return lista

resultado = Almacen()

while True:
    print("\n=== GESTOR DEL ALMACEN ===")
    print("1. Agregar unidades")
    print("2. Retirar unidades")
    print("3. Ver productos con pocas unidades")
    print("4. Ver todo el inventario")
    print("5. Salir")

    opcion = input("Ingrese una opción (1-5): ")

    match opcion:
        case "1":
            producto = input("Ingrese el producto: ").lower()
            cantidad = int(input("Ingrese la cantidad a agregar: "))

            resultado.agregar_unidades(producto, cantidad)

            print("Unidades agregadas correctamente.")

        case "2":
            producto = input("Ingrese el producto: ").lower()
            cantidad = int(input("Ingrese la cantidad a retirar: "))

            if resultado.retirar_unidades(producto, cantidad):
                print("True - Retiro realizado correctamente.")
            else:
                print("False - No hay suficientes unidades o el producto no existe.")

        case "3":
            limite = int(input("Ingrese el máximo de unidades para la alerta: "))

            productos = resultado.productos_agotados(limite)

            print(f"Productos con menos de {limite} unidades: {productos}")

        case "4":
            print(f"Inventario completo: {resultado.productos}")

        case "5":
            print("=== CERRANDO EL ALMACEN ===")
            break

        case _:
            print("Opción inválida.")
