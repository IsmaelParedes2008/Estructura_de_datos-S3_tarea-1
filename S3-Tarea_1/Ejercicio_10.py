""" Gestor de tareas con prioridad
Clase Tareas que: 
(1) tenga método agregar_tarea(descripcion, prioridad) que guarde en una lista de tuplas (descripción, prioridad); 
(2) tenga método tareas_prioritarias() que retorne solo las de prioridad alta; 
(3) tenga método eliminar_completada(descripcion) que borre la tarea de la lista.
Entrada
descripciones y prioridades
Proceso
guardar tuplas, filtrar por prioridad, eliminar
Salida
tareas filtradas
Ejemplo de entrada
t = Tareas()
t.agregar_tarea("Estudiar", "alta")
t.agregar_tarea("Leer", "baja")
t.tareas_prioritarias()
Salida esperada
[("Estudiar", "alta")]
💡 Colecciones: lista de tuplas (inmutables, ordenadas) """

class Tareas:
    def __init__(self):
        self.lista_tarea = []

    def agregar_tarea(self, descripcion, prioridad):
        self.lista_tarea.append((descripcion, prioridad))

    def tareas_prioritarias(self):
        listaP = []
        for descripcion, prioridad in self.lista_tarea:
            if prioridad.lower() == "alta":
                listaP.append((descripcion, prioridad))
        return listaP

    def eliminar_completada(self, borrarC):
        for descripcion, prioridad in self.lista_tarea:
            if descripcion.lower() == borrarC.lower():
                self.lista_tarea.remove((descripcion, prioridad))
                return True 
        return False 


resultado = Tareas()

while True:
    print("\n === GESTOR DE TAREAS CON PRIORIDAD ===")
    print("1. Agregar una tarea")
    print("2. Ver solo las tareas con prioridad ALTA")
    print("3. Eliminar una tarea completada")
    print("4. Ver todas las tareas de la lista")
    print("5. Salir")

    opcion = input("Ingrese una opción (1-5): ")

    match opcion:
        case "1":
            descripcion = input("Ingrese la descripción de la tarea: ")
            prioridad = input("Ingrese la prioridad (alta / media / baja): ")
            
            resultado.agregar_tarea(descripcion, prioridad)
            print(f"¡Tarea '{descripcion}' agregada con éxito!")

        case "2":
            prioritarias = resultado.tareas_prioritarias()
            print(f"\nTareas prioritarias (Alta): {prioritarias}")

        case "3":
            tarea_a_borrar = input("Ingrese la descripción de la tarea completada que desea borrar: ")
            if resultado.eliminar_completada(tarea_a_borrar):
                print(f"¡La tarea '{tarea_a_borrar}' fue eliminada de la lista con éxito!")
            else:
                print("No se encontró ninguna tarea con esa descripción.")

        case "4":
            print(f"\nLista completa de tareas actuales: {resultado.lista_tarea}")

        case "5":
            print("=== CERRANDO GESTOR DE TAREAS ===")
            break

        case _:
            print("Opción inválida. Intente de nuevo.")
