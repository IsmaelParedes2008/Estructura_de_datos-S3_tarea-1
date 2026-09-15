""" Estadísticas de temperatura
Clase GestorTemperatura que: (1) tenga método registrar_temperatura(temp) que guarde en una lista; 
(2) tenga método minima()`, `maxima()`, `promedio() que calculen estadísticas; 
(3) tenga método registrar_multiples(*temps) que reutilice el registro para varias temperaturas.
Entrada
temperaturas individuales o en lote
Proceso
guardar, calcular mín, máx, promedio
Salida
valores estadísticos
Ejemplo de entrada
gt = GestorTemperatura()
gt.registrar_multiples(20,25,18,30)
gt.promedio()
Salida esperada
23.25
💡 Colecciones: lista de números + funciones built-in min/max """

class Gestor_Temperatura:
    def __init__(self):
        self.historial_temperatura = []

    def Registrar_temperatura(self, temperatura):
        self.historial_temperatura.append(temperatura)

    def registrar_varias(self, *args):
        for i in args:
            self.Registrar_temperatura(i)

    def temperatura_min(self):
        if len(self.historial_temperatura) == 0:
            return 0
        return min(self.historial_temperatura)

    def temperatura_max(self):
        if len(self.historial_temperatura)==0:
            return 0
        return max(self.historial_temperatura)

    def promedio_temperatura(self):
        if len(self.historial_temperatura) == 0:
            return 0.0
        return sum(self.historial_temperatura)/len(self.historial_temperatura)

resultado = Gestor_Temperatura()
while True:
    print("1. Registrar lote de temperaturas.")
    print("2. Ver estadísticas (Mínima, Máxima, Promedio).")
    print("3. Ver historial de temperaturas.")
    print("4. Salir.")

    opcion = input("Ingrese una opción (1-4): ")

    match opcion:
        case "1":
            entrada = input("Ingrese las temperaturas separadas por espacio ( ) o por coma(,): ")
            temperatura_tex = entrada.replace(",", " ").split()

            temperatura = [float(i) for i in temperatura_tex]
            resultado.registrar_varias(*temperatura)

            print("Registro exitoso.")

        case "2":
            print(f"A. Temperatura minima. {resultado.temperatura_min()}")
            print(f"B. Temperatura maxima. {resultado.temperatura_max()}")
            print(f"C. Temperatura promedio. {resultado.promedio_temperatura():.2f}")

        case "3":
            print(f"Historial de temperatura: {resultado.historial_temperatura}")

        case "4":
            print("===CERRANDO PROGRAMa===")
            break
        
        case _:
            print("Opcion invalida.")




