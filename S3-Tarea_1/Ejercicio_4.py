""" EJERCICIO 4
Inversor de secuencias
Clase InversorSecuencia que: (1) tenga método invertir_lista(lista) que retorne la lista invertida sin usar reversed() (usa manual con bucles); 
(2) tenga método invertir_multiples(*listas) que reutilice el anterior para invertir varias listas y retorne un 
diccionario {lista_original: lista_invertida}.
Entrada
lista o varias listas
Proceso
invertir manualmente, guardar en diccionario
Salida
lista invertida o diccionario
Ejemplo de entrada
inv = InversorSecuencia()
inv.invertir_lista([1,2,3])
Salida esperada
[3, 2, 1]
💡 Colecciones: listas y diccionarios con tuplas como claves """

class Inversor_secuencia:
    def __init__(self):
        pass

    def invertir_lista(self, lista):
        lista_invertida = []

        for i in range(len(lista) -1, -1, -1):
            lista_invertida.append(lista[i])

        return lista_invertida

    def invertir_multiples(self, *lista):

        diccionario_exe = {}

        for i in lista:
            invertida = self.invertir_lista(i)

            tupla = tuple(i)

            diccionario_exe[tupla] = invertida

        return diccionario_exe
    
resultado = Inversor_secuencia()

while True:
    print("\n === INVERSOR DE SECUENCIAS ===")
    print("1. Invertir una sola lista de números")
    print("2. Invertir múltiples lotes de listas (*args)")
    print("3. Salir")
    
    opcion = input("Seleccione una opción (1-3): ")
    
    match opcion:
        case "1":
            entrada = input("Ingrese los digitos separados por espacio ( ) o por coma (,): ")
            digitos = entrada.replace(",", " ").split()

            resultado_simple = resultado.invertir_lista(digitos)

            print(f"Lista invertida manualmente: {resultado_simple}")

        case "2":
            n = int(input("¿Cuántos lotes de listas desea registrar?: "))
            lista_de_lotes = []

            for i in range(n):
                entrada = input("Ingrese los digitos separados por espacio ( ) o por coma (,): ")
                digitos = entrada.replace(",", " ").split()

                lote_dig = [int(x) for x in digitos]

                lista_de_lotes.append(lote_dig)

            resultadoDic = resultado.invertir_multiples(*lista_de_lotes)
            print(f"\nDiccionario invertido final: {resultadoDic}")

        case "3":
            print("===CERRANDO PROGRAMA===")
            break

        case _:
            print("Opcion invalida.")