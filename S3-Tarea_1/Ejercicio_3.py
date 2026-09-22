""" EJERCICIO 3
Gestor de compras con totales
Clase CarroCompras que: (1) tenga método agregar_articulo(nombre, precio) que guarde en un 
diccionario {nombre: precio}; 
(2) tenga método total_carrito() que retorne la suma de todos los precios; 
(3) tenga método articulos_por_rango(precio_min, precio_max) que retorne una lista 
con artículos dentro del rango.
Entrada
nombres de artículos y precios
Proceso
guardar en diccionario, sumar valores, filtrar por rango
Salida
total, artículos en rango
Ejemplo de entrada
c = CarroCompras()
c.agregar_articulo("pan",2.50)
c.agregar_articulo("leche",3.00)
c.total_carrito()
Salida esperada
5.50
💡 Colecciones: diccionario para almacenar nombre→precio """

class Carro_compra:
    def __init__(self):
        self.carrito_diccionario = {}

    def Agregar_articulo(self, nombre, precio):
        self.carrito_diccionario[nombre] = precio

    def Total_carrito(self):
        sum = 0

        for i in self.carrito_diccionario.values():
            sum += i

        return sum

    def Articulo_rango(self, precioMi, precioMa):
        lista = []


        for nombre, precio in self.carrito_diccionario.items():
            if precioMi <= precio <= precioMa:
                lista.append(nombre)

        return lista

resultado = Carro_compra()
while True:
    print("\n ===MENU DEl CARRO DE COMPRA===")
    print("1. Registrar productos.")
    print("2. Suma total de productos.")
    print("3. Filtrar artículos por rango de precio.")
    print("4. Ver carrito completo.")
    print("5. Salir")

    opcion = input("Ingrese una opcion del menu (1-5): ")

    match opcion:

        case "1":
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            resultado.Agregar_articulo(nombre, precio)
            print(f"¡Se realizó con éxito el registro de {nombre}!")

        case "2":
            total = resultado.Total_carrito()
            print(f"El valor total del carrito es: ${total}")

        case "3":
            precioMi = int(float("Ingrese el percio minimo a filtrar: "))
            precioMa = int(float("Ingrese el precio maximo a filtrar: "))

            resultado_rango = resultado.Articulo_rango(precioMi, precioMa)
            print(f"Productos en ese rango de precio: {resultado_rango}")

        case "4":
            print(f"Carrito de compra completo: {resultado.carrito_diccionario}")

        case "5":
            print("===CERRANDO PROGRAMA===")
            break

        case _:
            print("Opcion invalida.")


#EJERCICIO SIMILAR
"""Gestor de calificaciones

Crear una clase RegistroCalificaciones que:

Tenga un método agregar_estudiante(nombre, nota) que guarde en un diccionario:

nombre → nota
Tenga un método promedio_notas() que retorne el promedio de todas las notas registradas.
Tenga un método estudiantes_por_rango(nota_min, nota_max) que retorne una lista con los nombres de los estudiantes cuyas notas estén dentro del rango indicado.
Entrada

Nombres de estudiantes y sus notas.

Proceso

Guardar en un diccionario, sumar las notas, calcular promedio y filtrar estudiantes por rango.

Salida
Promedio de las notas.
Estudiantes que estén dentro de un rango de notas."""

class RegistroCalificaciones:
    def __init__(self):
        self.estudiantes = {}

    def agregar_estudiante(self, nombre, nota):
        self.estudiantes[nombre] = nota

    def promedio_notas(self):
        if len(self.estudiantes) == 0:
            return 0

        suma = 0

        for i in self.estudiantes.values():
            suma += i

        return suma / len(self.estudiantes)

    def estudiantes_por_rango(self, nota_min, nota_max):
        lista = []

        for nombre, nota in self.estudiantes.items():
            if nota_min <= nota <= nota_max:
                lista.append(nombre)

        return lista

resultado = RegistroCalificaciones()

while True:
    print("\n=== MENU DE REGISTRO DE CALIFICACIONES ===")
    print("1. Registrar estudiante")
    print("2. Ver promedio de notas")
    print("3. Filtrar estudiantes por rango")
    print("4. Ver estudiantes registrados")
    print("5. Salir")

    opcion = input("Ingrese una opcion (1-5): ")

    match opcion:

        case "1":
            nombre = input("Ingrese el nombre del estudiante: ")
            nota = float(input("Ingrese la nota del estudiante: "))

            resultado.agregar_estudiante(nombre, nota)

            print(f"Estudiante {nombre} registrado con exito.")

        case "2":
            promedio = resultado.promedio_notas()
            print(f"El promedio de las notas es: {promedio}")

        case "3":
            nota_min = float(input("Ingrese la nota minima: "))
            nota_max = float(input("Ingrese la nota maxima: "))

            estudiantes_rango = resultado.estudiantes_por_rango(nota_min, nota_max)

            print(f"Estudiantes dentro del rango: {estudiantes_rango}")

        case "4":
            print(f"Estudiantes registrados: {resultado.estudiantes}")

        case "5":
            print("=== CERRANDO PROGRAMA ===")
            break

        case _:
            print("Opcion invalida.")
