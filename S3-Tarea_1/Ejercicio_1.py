""" Validador de notas con promedio
Clase Calificador que: (1) tenga método validar_nota(nota) que retorne True si 0 ≤ nota ≤ 100, False en caso contrario; 
(2) tenga método cargar_notas(*args) que reciba múltiples notas, las valide, agregue solo las válidas a una lista interna, y retorne esa lista; 
(3) tenga método promedio() que retorne el promedio de notas almacenadas.
Entrada
notas individuales o en lotes (*args)
Proceso
validar cada nota (0-100), guardar en lista, calcular promedio
Salida
True/False, lista de válidas, promedio
Ejemplo de entrada
c = Calificador()
c.cargar_notas(85, 92, 110, 78, -5, 88)
c.promedio() """

class calificador:
    def __init__(self):
        self.historial_notas = []

    def validar_nota(self, notas):
        if 0<=notas<=100:
            return True
        else:
            return False

    def cargar_notas(self, *args):
        validas_notas = []

        for i in args:
            if self.validar_nota(i):
                self.historial_notas.append(i)
                validas_notas.append(i)
        return validas_notas

    def promedio(self):
        if len(self.historial_notas) == 0:
            return 0.0
        suma = 0

        for i in self.historial_notas:
            suma += i

        total_notas = len(self.historial_notas)
        return suma/total_notas

resultado = calificador()

while True:
    print("\n ===MENU DEL CALIFICADOR===")
    print("1. Registre notas individuales o por lotes.")
    print("2. Ver promedio de notas validas")
    print("3. Ver historial de las notas registradas")
    print("4. Salir")

    opcion = input("Ingrese una opcion del menu (1-4): ")

    match opcion:
        case "1":
            entrada = input("Ingrese la o las calificaciones separadas por espacio o por comas: ")
            notas_texto = entrada.replace(",", " ").split()

            lista_calificaciones = [int(i) for i in notas_texto]

            calificaciones_validas = resultado.cargar_notas(*lista_calificaciones)

            print(f"Calificaciones validas ingresadas {calificaciones_validas}")

        case "2":
            valor_promedio = resultado.promedio()

            print(f"El promedio de la lista de calificaciones es: {valor_promedio}")

        case "3":
            print(f"El historial de las calificaciones validas ingresadas es: {resultado.historial_notas}")

        case "4":
            print("===SALIENDO===")
            break

        case _:
            print("Opcion invalida.")



#EJERCCICIO SIMILAR:
class ValidadorEdades:
    def __init__(self):
        self.historial_edades = []

    def validar_edad(self, edad):
        if 1 <= edad <= 100:
            return True
        else:
            return False

    def cargar_edades(self, *args):
        edades_validas = []

        for edad in args:
            if self.validar_edad(edad):
                self.historial_edades.append(edad)
                edades_validas.append(edad)

        return edades_validas

    def promedio(self):
        if len(self.historial_edades) == 0:
            return 0.0

        suma = 0

        for edad in self.historial_edades:
            suma += edad

        total_edades = len(self.historial_edades)

        return suma / total_edades


resultado = ValidadorEdades()

while True:
    print("\n=== MENU DEL VALIDADOR DE EDADES ===")
    print("1. Registrar edades")
    print("2. Ver promedio")
    print("3. Ver historial")
    print("4. Salir")

    opcion = input("Ingrese una opcion (1-4): ")

    match opcion:
        case "1":
            entrada = input("Ingrese edades separadas por espacios o comas: ")

            edades_texto = entrada.replace(",", " ").split()

            lista_edades = [int(i) for i in edades_texto]

            edades_validas = resultado.cargar_edades(*lista_edades)

            print(f"Edades validas ingresadas: {edades_validas}")

        case "2":
            valor_promedio = resultado.promedio()

            print(f"El promedio de las edades es: {valor_promedio}")

        case "3":
            print(f"Historial de edades validas: {resultado.historial_edades}")

        case "4":
            print("=== SALIENDO ===")
            break

        case _:
            print("Opcion invalida.")
