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

#EJERCICIO SIMILAR
"""Múltiplos de un número

Clase MultiploFinder que:

Tenga un método encontrar_multiplos(numero, limite) que retorne una tupla con todos los múltiplos del número hasta el límite indicado.
Tenga un método es_multiplo(numero, valor) que retorne True si valor es múltiplo de numero.
Tenga un método encontrar_multiples_numeros(*numeros) que retorne un diccionario {número: tupla_multiplos}.

Entrada:
Uno o varios números.

Proceso:
Encontrar múltiplos mediante ciclos y verificar si un número es múltiplo de otro.

Salida:
Tuplas, booleano y diccionario."""

class MultiploFinder:
    def __init__(self):
        pass

    def encontrar_multiplos(self, numero, limite):
        lista_multiplos = []

        for i in range(1, limite + 1):
            if i % numero == 0:
                lista_multiplos.append(i)

        return tuple(lista_multiplos)

    def es_multiplo(self, numero, valor):
        if valor % numero == 0:
            return True
        else:
            return False

    def encontrar_multiples_numeros(self, *numeros):
        diccionario_multiplos = {}

        for numero in numeros:
            limite = int(input(f"Ingrese el límite para {numero}: "))

            lista = self.encontrar_multiplos(numero, limite)

            diccionario_multiplos[numero] = lista

        return diccionario_multiplos

resultado = MultiploFinder()

while True:
    print("\n=== FINDER DE MÚLTIPLOS ===")
    print("1. Encontrar múltiplos de un número")
    print("2. Verificar si un número es múltiplo de otro")
    print("3. Encontrar múltiples números a la vez")
    print("4. Salir")

    opcion = input("Ingrese una opción (1-4): ")

    match opcion:
        case "1":
            numero = int(input("Ingrese el número: "))
            limite = int(input("Ingrese el límite: "))

            multiplos = resultado.encontrar_multiplos(numero, limite)

            print(f"Múltiplos de {numero} hasta {limite}: {multiplos}")

        case "2":
            numero = int(input("Ingrese el número base: "))
            valor = int(input("Ingrese el valor a comprobar: "))

            if resultado.es_multiplo(numero, valor):
                print(f"{valor} SÍ es múltiplo de {numero}.")
            else:
                print(f"{valor} NO es múltiplo de {numero}.")

        case "3":
            entrada = input("Ingrese los números separados por espacios o comas: ")
            texto = entrada.replace(",", " ").split()

            lista_numeros = [int(i) for i in texto]

            resultado_diccionario = resultado.encontrar_multiples_numeros(*lista_numeros)

            print("\nDiccionario de múltiplos:")
            print(resultado_diccionario)

        case "4":
            print("=== CERRANDO PROGRAMA ===")
            break

        case _:
            print("Opción inválida. Intente de nuevo.")
