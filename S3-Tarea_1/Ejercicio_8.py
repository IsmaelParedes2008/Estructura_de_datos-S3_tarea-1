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


#EJERCICIO SIMILARES
"""GRUPOS

Crear una clase Grupos que:

crear_grupo(nombre_grupo) → cree un grupo con una lista vacía en un diccionario.
agregar_miembro(grupo, miembro) → agregue un miembro al grupo.
grupo_mayor_miembros() → retorne el nombre del grupo que tenga más miembros."""

class Grupos:
    def __init__(self):
        self.diccionario_miembros = {}

    def crear_grupo(self, nombre_grupo):
        self.diccionario_miembros[nombre_grupo] = []

    def agregar_miembro(self, grupo, miembro):
        if grupo in self.diccionario_miembros:
            self.diccionario_miembros[grupo].append(miembro)
        else:
            print(f"Error: El grupo '{grupo}' no existe.")

    def grupo_mayor_miembros(self):
        if len(self.diccionario_miembros) == 0:
            return 0

        nombre_grupo = ""
        max_miembros = -1

        for grupo, lista_miembros in self.diccionario_miembros.items():
            if len(lista_miembros) > max_miembros:
                max_miembros = len(lista_miembros)
                nombre_grupo = grupo

        return nombre_grupo

resultado = Grupos()

while True:
    print("\n=== GRUPOS ===")
    print("1. Crear grupo")
    print("2. Agregar miembro")
    print("3. Grupo con más miembros")
    print("4. Ver grupos")
    print("5. Salir")

    opcion = input("Ingrese una opción: ")

    match opcion:
        case "1":
            nombre = input("Ingrese el nombre del grupo: ")
            resultado.crear_grupo(nombre)
            print("Grupo creado correctamente.")

        case "2":
            grupo = input("Ingrese el grupo: ")
            miembro = input("Ingrese el nombre del miembro: ")
            resultado.agregar_miembro(grupo, miembro)

        case "3":
            print(f"Grupo con más miembros: {resultado.grupo_mayor_miembros()}")

        case "4":
            print(resultado.diccionario_miembros)

        case "5":
            print("=== CERRANDO PROGRAMA ===")
            break

        case _:
            print("Opción inválida.")
