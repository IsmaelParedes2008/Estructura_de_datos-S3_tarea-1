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

#    def registrar_multiples(self, lista_estudiantes):
#        for i in lista_estudiantes:
#            partes = i.split(":")
#            
#            if len(partes) == 2:
#                nombre = partes[0]
#                nota = int(partes[1]) 
#                
#                self.registrar(nombre, nota)

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























#case "1":
#            print("\n--- REGISTRO DE ESTUDIANTES ---")
#            print("A. Registrar un solo estudiante")
#            print("B. Registrar lote de estudiantes")
#            sub_opcion = input("Elija una opción (A/B): ").upper()
#
#            if sub_opcion == "A":
#                nombre = input("Ingrese el nombre del estudiante: ")
#                nota = int(input("Ingrese la nota del estudiante (0-100): "))
#                resultado.registrar(nombre, nota)
#                print(f"¡Estudiante {nombre} registrado con éxito!")
#
#            elif sub_opcion == "B":
#                entrada = input("Ingrese los estudiantes en formato nombre:nota separados por espacios\n(Ejemplo: Ana:95 Bob:70 Carlos:88):\n> ")
#                
#                # Separamos el texto por espacios para obtener una lista de textos
#                lote_texto = entrada.split()
#                
#                # Le pasamos la lista a tu nuevo método
#                resultado.registrar_multiples(lote_texto)
#                print("¡Lote de estudiantes registrado con éxito!")
#            else:
#                print("Opción inválida.")