""" Básico
Mapeador de edades
Clase GestorPersonas que: (1) tenga método agregar_persona(nombre, edad) que guarde en un diccionario; 
(2) tenga método personas_mayores(edad_minima) que retorne una lista de nombres cuya edad sea ≥; 
(3) tenga método edad_promedio() que retorne el promedio de edades.
Entrada
nombres y edades
Proceso
guardar en diccionario, filtrar, promediar
Salida
lista filtrada, promedio
Ejemplo de entrada
gp = GestorPersonas()
gp.agregar_persona("Ana",28)
gp.agregar_persona("Bob",17)
gp.personas_mayores(18)
Salida esperada
["Ana"]
💡 Colecciones: diccionario nombre→edad, iteración con items() """

class Gestor_persona:
    def __init__(self):
        self.persona_diccionario = {}

    def agregar_persona(self, nombre, edad):
        self.persona_diccionario[nombre]=edad

  #  def agregar_multiples(self, lista_personas):
  #      
  #      for i in lista_personas:
  #          partes = i.split(":")
#
  #          if len(partes) == 2:
  #              nombre = partes[0]
  #              edad = int(partes[1])
  #              self.agregar_persona(nombre, edad)

    def persona_mayores(self, edad_minima):
        lista_mayores = []

        for nombre, edad in self.persona_diccionario.items():
            if edad >= edad_minima:
                lista_mayores.append(nombre)
        return lista_mayores

    def edad_promedio(self):
        if len(self.persona_diccionario) == 0:
            return 0.0

        suma = 0

        for i in self.persona_diccionario.values():
            suma += i

        total_personas = len(self.persona_diccionario)

        return suma/total_personas

resultado = Gestor_persona()
while True:
    print("\n ===MENU DEL GESTOR===")
    print("1. Registrar personas.")
    print("2. Filtrar personas mayores o iguales a una edad.")
    print("3. Ver edad promedio.")
    print("4. Ver lista completa de personas.")
    print("5. Salir")

    opcion = input("Ingrese una opción (1-5): ")

    match opcion:
        case "1":
            nombre = input("Ingrese el nombre de la persona: ")
            edad = int(input("Ingrese la edad de la persona: ")) 

            resultado.agregar_persona(nombre, edad)

   #        case "1":
   #            print("\n--- REGISTRO DE PERSONAS ---")
   #            print("A. Registrar una sola persona")
   #            print("B. Registrar lote de personas")
   #            sub_opcion = input("Elija una opción (A/B): ").upper()

   #            if sub_opcion == "A":
   #                nombre = input("Ingrese el nombre de la persona: ")
   #                edad = int(input("Ingrese la edad de la persona: "))
   #                resultado.agregar_persona(nombre, edad)
   #                print(f"¡{nombre} registrado con éxito!")

   #            elif sub_opcion == "B":
   #                entrada = input("Ingrese las personas en formato nombre:edad separadas por espacios\n(Ejemplo: Ana:28 Bob:17 Carlos:30):\n> ")
   #            
   #                lote_texto = entrada.split()
   #            
   #                resultado.agregar_multiples(lote_texto)
   #                print("¡Lote de personas registrado con éxito!")
   #            else:
   #                print("Opción inválida.")


        case "2":
            limite = int(input("Ingrese la edad mínima para filtrar: "))
            mayores = resultado.persona_mayores(limite)

            print(f"Personas con edad mayor o igual a {limite}: {mayores}")

        case "3":
            promedio = resultado.edad_promedio()
            print(f"La edad promedio es: {promedio:.2f} años")

        case "4":
            print(f"Diccionario de personas registradas: {resultado.persona_diccionario}")

        case "5":
            print("=== CERRANDO PROGRAMA ===")
            break

        case _:
            print("Opción inválida. Intente de nuevo.")   


#EJERCICIO SIMILAR
"""Gestor de Productos

Este usa la misma estructura, pero cambiamos personas/edades por productos/precios.

Enunciado corto

Crear una clase GestorProductos que:

Guarde nombre → precio en un diccionario.
Tenga productos_mayores(precio_minimo) que retorne los nombres de productos cuyo precio sea >=.
Tenga precio_promedio() que calcule el promedio de precios."""

class Gestor_Productos:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, nombre, precio):
        self.productos[nombre] = precio

    def productos_mayores(self, precio_minimo):
        lista = []

        for nombre, precio in self.productos.items():
            if precio >= precio_minimo:
                lista.append(nombre)

        return lista

    def precio_promedio(self):
        if len(self.productos) == 0:
            return 0.0

        suma = 0

        for precio in self.productos.values():
            suma += precio

        return suma / len(self.productos)

resultado = Gestor_Productos()

while True:
    print("\n=== GESTOR DE PRODUCTOS ===")
    print("1. Registrar producto")
    print("2. Filtrar productos por precio")
    print("3. Ver precio promedio")
    print("4. Ver productos registrados")
    print("5. Salir")

    opcion = input("Ingrese una opción (1-5): ")

    match opcion:
        case "1":
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio: "))

            resultado.agregar_producto(nombre, precio)

            print("Producto registrado con éxito.")

        case "2":
            limite = float(input("Ingrese el precio mínimo: "))

            productos = resultado.productos_mayores(limite)

            print(f"Productos con precio mayor o igual a {limite}: {productos}")

        case "3":
            promedio = resultado.precio_promedio()

            print(f"El precio promedio es: {promedio:.2f}")

        case "4":
            print(f"Productos registrados: {resultado.productos}")

        case "5":
            print("=== CERRANDO PROGRAMA ===")
            break

        case _:
            print("Opción inválida.")


