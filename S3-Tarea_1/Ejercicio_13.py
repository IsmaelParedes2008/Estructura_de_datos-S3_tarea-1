""" Combinador de listas
Clase CombinadorListas que: 
(1) tenga método intercalar(lista1, lista2) que retorne una lista alternando elementos de ambas; 
(2) tenga método intercalar_multiples(*listas) que reutilice para varias listas.
Entrada
dos o más listas
Proceso
alternar elementos con índices, bucles
Salida
lista intercalada
Ejemplo de entrada
cl = CombinadorListas()
cl.intercalar([1,2], [3,4])
Salida esperada
[1, 3, 2, 4]
💡 Colecciones: indexación de listas con loops y condicionales """

class Combinar_listas:
    def __init__(self):
        pass

    def intercalar(self, lista1, lista2):
        lista_intercalada = []

        largoM = max(len(lista1), len(lista2))

        for i in range(largoM):

            if i < len(lista1):
                lista_intercalada.append(lista1[i])

            if i < len(lista2):
                lista_intercalada.append(lista2[i])
                
        return lista_intercalada

    def intercalar_multiples(self, *args):
        if len(args) == 0:
            return []
            
        resultado_final = args[0]
        
        for i in range(1, len(args)):
            resultado_final = self.intercalar(resultado_final, args[i])
            
        return resultado_final  

resultado = Combinar_listas()

while True:
    print("\n === COMBINADOR DE LISTAS ===")
    print("1. Intercalar dos listas de números")
    print("2. Intercalar múltiples listas (*args)")
    print("3. Salir")

    opcion = input("Ingrese una opción (1-3): ")

    match opcion:
        case "1":
            entrada1 = input("Ingrese la primera lista separada por espacios o comas: ")
            entrada2 = input("Ingrese la segunda lista separada por espacios o comas: ")
            
            texto1 = entrada1.replace(",", " ").split()
            texto2 = entrada2.replace(",", " ").split()

            lista1 = [int(i) for i in texto1]
            lista2 = [int(j) for j in texto2]
            
            resultado_simple = resultado.intercalar(lista1, lista2)
            print(f"\nLista intercalada final: {resultado_simple}")

        case "2":
            n = int(input("¿Cuántas listas desea intercalar en total?: "))
            lista_de_listas = []
            
            for i in range(n):
                entrada = input(f"Ingrese la lista {i+1} separada por espacios o comas: ")

                texto = entrada.replace(",", " ").split()
                lista_numeros = [int(x) for x in texto]
                
                lista_de_listas.append(lista_numeros)
                
            resultado_multiple = resultado.intercalar_multiples(*lista_de_listas)
            print(f"\nResultado intercalado de todas las listas: {resultado_multiple}")

        case "3":
            print("=== CERRANDO PROGRAMA ===")
            break

        case _:
            print("Opción inválida. Intente de nuevo.")

#EJERCICIO SIMILAR
"""Combinador de nombres
Clase CombinadorNombres que:
Tenga un método intercalar(lista1, lista2) que reciba dos listas de nombres y retorne una nueva lista alternando los elementos de ambas listas.
Tenga un método intercalar_multiples(*listas) que permita intercalar varias listas reutilizando el método intercalar().
Entrada:
Dos o más listas de nombres.
Proceso:
Alternar los elementos utilizando índices, ciclos y condicionales. Si una lista tiene más elementos que otra, agregar los elementos restantes.
Salida:
Una lista con los nombres intercalados.
Ejemplo de entrada:
cn = CombinadorNombres()
cn.intercalar(["Ana", "Luis"], ["Pedro", "María"])
Salida esperada:
["Ana", "Pedro", "Luis", "María"]"""

class CombinadorNombres:
    def __init__(self):
        pass

    def intercalar(self, lista1, lista2):
        lista_intercalada = []

        largoM = max(len(lista1), len(lista2))

        for i in range(largoM):

            if i < len(lista1):
                lista_intercalada.append(lista1[i])

            if i < len(lista2):
                lista_intercalada.append(lista2[i])

        return lista_intercalada

    def intercalar_multiples(self, *listas):
        if len(listas) == 0:
            return []

        resultado_final = listas[0]

        for i in range(1, len(listas)):
            resultado_final = self.intercalar(resultado_final, listas[i])

        return resultado_final


resultado = CombinadorNombres()

while True:
    print("\n=== COMBINADOR DE NOMBRES ===")
    print("1. Intercalar dos listas")
    print("2. Intercalar múltiples listas")
    print("3. Salir")

    opcion = input("Ingrese una opción (1-3): ")

    match opcion:
        case "1":
            entrada1 = input("Ingrese la primera lista de nombres separada por espacios: ")
            entrada2 = input("Ingrese la segunda lista de nombres separada por espacios: ")

            lista1 = entrada1.split()
            lista2 = entrada2.split()

            resultado_simple = resultado.intercalar(lista1, lista2)

            print(f"\nLista intercalada: {resultado_simple}")

        case "2":
            n = int(input("¿Cuántas listas desea intercalar?: "))
            lista_de_listas = []

            for i in range(n):
                entrada = input(f"Ingrese la lista {i + 1} de nombres: ")

                lista_nombres = entrada.split()
                lista_de_listas.append(lista_nombres)

            resultado_multiple = resultado.intercalar_multiples(*lista_de_listas)

            print(f"\nResultado intercalado: {resultado_multiple}")

        case "3":
            print("=== CERRANDO PROGRAMA ===")
            break

        case _:
            print("Opción inválida.")
