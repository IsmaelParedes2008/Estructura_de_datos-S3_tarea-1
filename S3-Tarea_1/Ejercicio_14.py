""" Mapeo de estudiantes a notas
Clase RegistroNotas que: 
(1) tenga método registrar(estudiante, nota) que guarde en un diccionario; 
(2) tenga método estudiantes_aprobados(nota_minima) que retorne lista de estudiantes; 
(3) tenga método mejor_estudiante() que retorne nombre y nota del que tiene mayor calificación.
Entrada
estudiante → nota
Proceso
guardar diccionario, iterar con items(), comparar
Salida
listas filtradas, tupla (nombre, nota)
Ejemplo de entrada
rn = RegistroNotas()
rn.registrar("Ana", 95)
rn.registrar("Bob", 70)
rn.mejor_estudiante()
Salida esperada
("Ana", 95)
💡 Colecciones: diccionario.items() para iterar clave-valor """

class Registro_notas:
    def __init__(self):
        self.diccionario_notas = {}

    def registrar(self, estudiante, nota):
        self.diccionario_notas[estudiante] = nota

    def estudiante_aprobado(self, nota_min):
        lista_aprob = []

        for estudiante, nota in self.diccionario_notas.items():
            if nota >= nota_min:
                lista_aprob.append(estudiante)
                
        return lista_aprob

    def mejor_estudiante(self):
        if len(self.diccionario_notas) == 0:
            return ("Ninguno", 0)
            
        estudiante_top = ""
        max_nota = -1
        
        for estudiante, nota in self.diccionario_notas.items():
            if nota > max_nota:
                max_nota = nota
                estudiante_top = estudiante
                
        return (estudiante_top, max_nota)

resultado = Registro_notas()

while True:
    print("\n === SISTEMA DE REGISTRO DE NOTAS ===")
    print("1. Registrar estudiante y nota")
    print("2. Ver lista de estudiantes aprobados")
    print("3. Ver quién es el mejor estudiante")
    print("4. Ver todo el registro de notas")
    print("5. Salir")

    opcion = input("Ingrese una opción del menú (1-5): ")

    match opcion:
        case "1":
            nombre = input("Ingrese el nombre del estudiante: ")
            nota = int(input("Ingrese la nota del estudiante (0-100): "))
            
            resultado.registrar(nombre, nota)
            print(f"¡Estudiante {nombre} registrado con éxito!")

        case "2":
            limite = int(input("Ingrese la nota mínima para aprobar: "))
            aprobados = resultado.estudiante_aprobado(limite)
            print(f"Estudiantes aprobados: {aprobados}")

        case "3":
            mejor = resultado.mejor_estudiante()
            print(f"El mejor estudiante actual es: {mejor}")

        case "4":
            print(f"Registro completo actual: {resultado.diccionario_notas}")

        case "5":
            print("=== CERRANDO SISTEMA DE NOTAS ===")
            break

        case _:
            print("Opción inválida. Intente de nuevo.")

#EJERCICIO SIMILAR
"""Registro de productos

Clase RegistroProductos que:

Tenga un método registrar(producto, precio) que guarde cada producto y su precio en un diccionario.
Tenga un método productos_caros(precio_minimo) que retorne una lista con los productos cuyo precio sea mayor o igual al mínimo indicado.
Tenga un método producto_mas_caro() que retorne una tupla con el nombre y precio del producto que tenga el mayor precio.

Entrada:
Producto → precio.

Proceso:
Guardar los datos en un diccionario, recorrerlo utilizando .items() y comparar los precios.

Salida:
Lista de productos filtrados y tupla (producto, precio) del producto más caro."""

class RegistroProductos:
    def __init__(self):
        self.diccionario_productos = {}

    def registrar(self, producto, precio):
        self.diccionario_productos[producto] = precio

    def productos_caros(self, precio_minimo):
        lista_caros = []

        for producto, precio in self.diccionario_productos.items():
            if precio >= precio_minimo:
                lista_caros.append(producto)

        return lista_caros

    def producto_mas_caro(self):
        if len(self.diccionario_productos) == 0:
            return ("Ninguno", 0)

        producto_top = ""
        max_precio = -1

        for producto, precio in self.diccionario_productos.items():
            if precio > max_precio:
                max_precio = precio
                producto_top = producto

        return (producto_top, max_precio)


resultado = RegistroProductos()

while True:
    print("\n=== REGISTRO DE PRODUCTOS ===")
    print("1. Registrar producto")
    print("2. Ver productos caros")
    print("3. Ver producto más caro")
    print("4. Ver todos los productos")
    print("5. Salir")

    opcion = input("Ingrese una opción (1-5): ")

    match opcion:
        case "1":
            producto = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio: "))

            resultado.registrar(producto, precio)
            print("Producto registrado correctamente.")

        case "2":
            minimo = float(input("Ingrese el precio mínimo: "))

            caros = resultado.productos_caros(minimo)
            print(f"Productos con precio mayor o igual a {minimo}: {caros}")

        case "3":
            mejor = resultado.producto_mas_caro()
            print(f"Producto más caro: {mejor}")

        case "4":
            print(f"Registro completo: {resultado.diccionario_productos}")

        case "5":
            print("=== CERRANDO PROGRAMA ===")
            break

        case _:
            print("Opción inválida.")
