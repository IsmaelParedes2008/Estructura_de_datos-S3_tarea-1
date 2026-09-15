""" EJERCICIO 0
Enunciado. Crear una clase NumeroPrimo que:
Tenga un método es_primo(numero) que retorne True o False.
Tenga un método primos_en_rango(*args) que reciba múltiples números y retorne una lista con los 
que son primos, reutilizando es_primo().
Tenga un atributo historial (una lista) que guarde todos los números probados.
Tenga un método cantidad_verificados() que retorne cuántos números se han probado. """

class NumeroPrimo:
    """Clase para validar números primos y guardar historial de búsquedas."""
    
    def __init__(self):
        self.historial = []

    def es_primo(self, numero):
        self.historial.append(numero)
        if numero < 2:
            return False
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                return False
        return True

    def primos_en_rango(self, *args):
        primos = []
        for i in args:
            if self.es_primo(i):
                primos.append(i)
        return primos

    def primos_hasta(self, n):
        primos = []
        for i in range(2, n + 1):
            if self.es_primo(i):
                primos.append(i)
        return primos

    def cantidad_por_rango(self, inicio, fin):
        contador = 0
        for i in range(inicio, fin + 1):
            if self.es_primo(i):
                contador += 1
        return contador

    def cantidad_verificados(self):
        return len(self.historial)

    def limpiar_historial(self):
        self.historial = []


# --- Programa principal interactivo ---
np = NumeroPrimo()

while True:
    print("\n--- MENÚ DE NÚMEROS PRIMOS ---")
    print("1. Verificar si un número es primo")
    print("2. Verificar múltiples números (primos en rango)")
    print("3. Ver todos los primos hasta N")
    print("4. Contar primos en un rango (Inicio - Fin)")
    print("5. Ver historial de números verificados")
    print("6. Limpiar historial")
    print("7. Salir")
    
    opcion = input("Selecciona una opción (1-7): ")
    
    match opcion:
        case "1":
            num = int(input("Ingresa el número a verificar: "))
            if np.es_primo(num):
                print(f"¡El número {num} SÍ es primo!")
            else:
                print(f"El número {num} NO es primo.")
                
        case "2":
            
            n = int(input("Ingrese cuántos números quiere verificar: "))
            lista_numeros = []

            for i in range(n):
                num = int(input(f"Ingrese el número {i+1}: "))
                lista_numeros.append(num)

            resultado = np.primos_en_rango(*lista_numeros)
            print(f"Los números primos entre los ingresados son: {resultado}")
            
        case "3":
            limite = int(input("Ingresa el número límite (N): "))
            resultado = np.primos_hasta(limite)
            print(f"Los números primos hasta {limite} son: {resultado}")
            
        case "4":
            inicio = int(input("Ingresa el número de inicio del rango: "))
            fin = int(input("Ingresa el número de fin del rango: "))
            cantidad = np.cantidad_por_rango(inicio, fin)
            print(f"Hay un total de {cantidad} números primos entre {inicio} y {fin}.")
            
        case "5":
            print(f"Historial actual: {np.historial}")
            print(f"Total de verificaciones realizadas: {np.cantidad_verificados()}")
            
        case "6":
            np.limpiar_historial()
            print("El historial ha sido borrado con éxito.")
            
        case "7":
            print("¡Gracias por usar el programa! Hasta luego.")
            break
            
        case _:
            print("Opción no válida. Por favor, intenta de nuevo.")
