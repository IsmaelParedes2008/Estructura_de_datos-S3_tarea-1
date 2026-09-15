
""" Contador de frecuencia
Clase ContadorFrecuencia que: 
(1) tenga método agregar_elemento(elemento) que guarde en un diccionario contando repeticiones; 
(2) tenga método elemento_mas_frecuente() que retorne el elemento con mayor frecuencia; 
(3) tenga método frecuencia_elemento(elemento) que retorne cuántas veces aparece.
Entrada
elementos individuales o en lote
Proceso
guardar en diccionario, contar, encontrar máximo
Salida
elemento más frecuente y su conteo
Ejemplo de entrada
cf = ContadorFrecuencia()
cf.agregar_elemento("a")
cf.agregar_elemento("b")
cf.agregar_elemento("a")
cf.elemento_mas_frecuente()
Salida esperada
"a"
💡 Colecciones: diccionario como contador (patrón común) """
class ContadorFrecuencia:
    def __init__(self):
        self.registro_frecuencia = {}

    def agregar_elemento(self, elemento):
        if elemento in self.registro_frecuencia:
            self.registro_frecuencia[elemento] += 1
        else:
            self.registro_frecuencia[elemento] = 1

    def elemento_mas_frecuente(self):
        if len(self.registro_frecuencia) == 0:
            return "No hay frecuencia"

        frecuencia = ""
        max_frecuencia = -1

        for elemento, cantidad in self.registro_frecuencia.items():
            if cantidad > max_frecuencia:
                max_frecuencia = cantidad
                frecuencia = elemento     

        return frecuencia

    def frecuencia_elemento(self, elemento):
        if elemento in self.registro_frecuencia:
            return self.registro_frecuencia[elemento]
        else:
            return 0


resultado = ContadorFrecuencia()

while True:
    print("\n === CONTADOR DE FRECUENCIA ===")
    print("1. Registrar elementos (Individual o por lote)")
    print("2. Ver el elemento más frecuente")
    print("3. Consultar frecuencia de un elemento específico")
    print("4. Ver diccionario completo")
    print("5. Salir")

    opcion = input("Ingrese una opción (1-5): ")

    match opcion:
        case "1":
            entrada = input("Ingrese los elementos separados por espacio( ) o por comas(,): ")
            elemento_tex = entrada.replace(",", " ").split()

            for i in elemento_tex:
                resultado.agregar_elemento(i)

            print("¡Elementos registrados con éxito!")

        case "2":
            maxF = resultado.elemento_mas_frecuente()
            print(f"El elemento con más frecuencia es: {maxF}")

        case "3":
            buscar = input("¿Qué elemento desea consultar?: ")
            cant_repeticiones = resultado.frecuencia_elemento(buscar)
            print(f"El elemento '{buscar}' aparece {cant_repeticiones} veces.")

        case "4":
            print(f"Diccionario de frecuencias actual: {resultado.registro_frecuencia}")

        case "5":
            print("=== CERRANDO PROGRAMA ===")
            break

        case _:
            print("Opción inválida. Intente de nuevo.")
