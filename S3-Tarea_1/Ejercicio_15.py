""" Divisores de un número
Clase DivisorFinder que: 
(1) tenga método encontrar_divisores(numero) que retorne una tupla con todos los divisores; 
(2) tenga método es_perfecto(numero) que retorne True si la suma de sus divisores (excepto él mismo) es igual a él; 
(3) tenga método encontrar_multiples_divisores(*numeros) que retorne un diccionario {número: tupla_divisores}.
Entrada
uno o varios números
Proceso
encontrar divisores con bucles, verificar suma
Salida
tuplas, booleano, diccionario
Ejemplo de entrada
df = DivisorFinder()
df.encontrar_divisores(12)
Salida esperada
(1, 2, 3, 4, 6, 12)
💡 Colecciones: tuplas (inmutables), diccionario como almacén """

class divisor_finder:
    def __init__(self):
        pass

    def encontrar_divisores(self, numero):
        lista_divisores = []

        for i in range(1, numero + 1):
            if numero % i == 0:
                lista_divisores.append(i)

        return tuple(lista_divisores)
      
    def es_perfecto(self, numero):
        perfecto = self.encontrar_divisores(numero)
        
        suma = 0
        for i in perfecto:
            if i != numero:
                suma += i
                
        if suma == numero:
            return True
        else:
            return False            

    def multiples_divisores(self, *args):
        diccionario_divisores = {}
        
        for i in args:
            diccionario_divisores[i] = self.encontrar_divisores(i)
            
        return diccionario_divisores

resultado = divisor_finder()

while True:
    print("\n === FINDER DE DIVISORES ===")
    print("1. Encontrar divisores de un número (Tupla)")
    print("2. Verificar si un número es Perfecto (True/False)")
    print("3. Encontrar múltiples divisores a la vez (*args)")
    print("4. Salir")

    opcion = input("Ingrese una opción (1-4): ")

    match opcion:
        case "1":
            num = int(input("Ingrese un número entero positivo: "))
            rango_tupla = resultado.encontrar_divisores(num)
            print(f"\nDivisores de {num}: {rango_tupla}")

        case "2":
            num = int(input("Ingrese un número para verificar si es perfecto: "))
            if resultado.es_perfecto(num):
                print(f"¡El número {num} SÍ es un número perfecto!")
            else:
                print(f"El número {num} NO es un número perfecto.")

        case "3":
            entrada = input("Ingrese los números separados por espacios o comas: ")
            texto = entrada.replace(",", " ").split()
            
            lista_numeros = [int(i) for i in texto]
            
            resultado_diccionario = resultado.multiples_divisores(*lista_numeros)
            print(f"\nDiccionario resultante de divisores:\n{resultado_diccionario}")

        case "4":
            print("=== CERRANDO PROGRAMA ===")
            break

        case _:
            print("Opción inválida. Intente de nuevo.")