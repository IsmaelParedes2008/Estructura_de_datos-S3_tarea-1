""" Asignador de equipos
Clase Equipos que: 
(1) tenga método crear_equipo(nombre_equipo) que inicie un equipo como una lista vacía en un diccionario; 
(2) tenga método agregar_jugador(equipo, jugador) que añada el jugador al equipo; 
(3) tenga método equipo_mayor_integrantes() que retorne el nombre del equipo con más jugadores.
Entrada
nombres de equipos y jugadores
Proceso
crear estructura equipo→[jugadores], contar, comparar
Salida
equipo con mayor cantidad
Ejemplo de entrada
eq = Equipos()
eq.crear_equipo("A")
eq.agregar_jugador("A","Juan")
eq.agregar_jugador("A","Pedro")
Salida esperada
—
💡 Colecciones: diccionario de listas (estructura anidada) """

class Equipos:
    def __init__(self):
        self.diccionario_jugador = {}

    def crear_equipo(self, nombre_equipo):
        self.diccionario_jugador[nombre_equipo]=[]

    def agregar_jugador(self, equipo, jugador):
        if equipo in self.diccionario_jugador:
            self.diccionario_jugador[equipo].append(jugador)
        else:
            print(f"Error: El equipo '{equipo}' no existe. Créalo primero.")

 #   def crear_multiples_equipos(self, lista_nombres):
 #       for i in lista_nombres:
 #           self.crear_equipo(i)
#
 #   def agregar_lote_jugadores(self, equipo, lista_jugadores):
 #       if equipo in self.diccionario_jugador:
#
 #           for i in lista_jugadores:
 #               self.diccionario_jugador[equipo].append(i)
 #       else:
 #           print(f"Error: El equipo '{equipo}' no existe. Créalo primero.")

    def mayor_integrantes(self):
        if len(self.diccionario_jugador) == 0:
            return 0

        nombreJ = ""
        maxIntegrante = -1

        for equipo, lista_jugador in self.diccionario_jugador.items():
            if len(lista_jugador) > maxIntegrante:
                 maxIntegrante = len(lista_jugador)
                 nombreJ = equipo

        return nombreJ

resultado = Equipos()

while True:
    print("\n === GESTOR DE EQUIPOS ===")
    print("1. Crear un equipo nuevo")
    print("2. Agregar jugador a un equipo")
    print("3. Ver cuál equipo tiene más integrantes")
    print("4. Ver todos los equipos y sus jugadores")
    print("5. Salir")

    opcion = input("Ingrese una opción (1-5): ")

    match opcion:
        case "1":
            nombre_eq = input("Ingrese el nombre del equipo nuevo (ej: A, Barcelona, Madrid): ")
            resultado.crear_equipo(nombre_eq)

            print(f"¡Equipo '{nombre_eq}' creado con éxito como una lista vacía!")

        case "2":
            nombre_eq = input("¿A qué equipo desea añadir el jugador?: ")
            nombre_jug = input("Ingrese el nombre del jugador: ")
            resultado.agregar_jugador(nombre_eq, nombre_jug)
            print(f"¡Jugador {nombre_jug} asignado con éxito!")

        case "3":
            equipo_top = resultado.mayor_integrantes()
            print(f"El equipo con mayor cantidad de integrantes es: {equipo_top}")

        case "4":
            print("\n--- INVENTARIO DE EQUIPOS Y INTEGRANTES ---")
            for equipo, jugadores in resultado.diccionario_jugador.items():
                print(f"Equipo {equipo}: {jugadores} (Total: {len(jugadores)})")

        case "5":
            print("=== CERRANDO GESTOR DE EQUIPOS ===")
            break

        case _:
            print("Opción inválida. Intente de nuevo.")






            









 #case "1":
 #           print("\n--- CREACIÓN DE EQUIPOS ---")
 #           print("A. Crear un solo equipo")
 #           print("B. Crear múltiples equipos a la vez")
 #           sub_opcion = input("Elija una opción (A/B): ").upper()
#
 #           if sub_opcion == "A":
 #               nombre_eq = input("Ingrese el nombre del equipo nuevo: ")
 #               resultado.crear_equipo(nombre_eq)
 #               print(f"¡Equipo '{nombre_eq}' creado con éxito!")
#
 #           elif sub_opcion == "B":
 #               entrada = input("Ingrese los nombres de los equipos separados por espacios o comas\n(Ejemplo: A, B, Barcelona, Madrid):\n> ")
 #               # Limpiamos comas y separamos por espacios para tener una lista de nombres
 #               lote_equipos = entrada.replace(",", " ").split()
 #               
 #               resultado.crear_multiples_equipos(lote_equipos)
 #               print("¡Lote de equipos creado con éxito!")
 #           else:
 #               print("Opción inválida.")



# case "2":
#            print("\n--- ASIGNACIÓN DE JUGADORES ---")
#            print("A. Agregar un solo jugador")
#            print("B. Agregar lote de jugadores a un equipo")
#            sub_opcion = input("Elija una opción (A/B): ").upper()
#
#            if sub_opcion == "A":
#                nombre_eq = input("¿A qué equipo desea añadir el jugador?: ")
#                nombre_jug = input("Ingrese el nombre del jugador: ")
#                resultado.agregar_jugador(nombre_eq, nombre_jug)
#                print(f"¡Jugador {nombre_jug} asignado con éxito!")
#
#            elif sub_opcion == "B":
#                nombre_eq = input("¿A qué equipo desea añadir el lote de jugadores?: ")
#                entrada = input("Ingrese los nombres de los jugadores separados por espacios o comas\n(Ejemplo: Juan, Pedro, Lucas, Mateo):\n> ")
#                # Limpiamos comas y separamos por palabras
#                lote_jugadores = entrada.replace(",", " ").split()
#                
#                resultado.agregar_lote_jugadores(nombre_eq, lote_jugadores)
#                print(f"¡Lote de jugadores agregado con éxito al equipo {nombre_eq}!")
#            else:
#                print("Opción inválida.")