""" EJERCICIO 5
Detector de números pares e impares
Clase AnalizadorNumeros que: (1) tenga método es_par(numero) que retorne True/False; 
(2) tenga método separar(*numeros) que retorne un diccionario {'pares': [...], 'impares': [...]} reutilizando es_par; 
(3) tenga método cantidad_pares_impares() que retorne una tupla (cant_pares, cant_impares).
Entrada
números en lote
Proceso
clasificar pares e impares con operador %
Salida
diccionario y tupla con cantidades
Ejemplo de entrada
an = AnalizadorNumeros()
an.separar(1,2,3,4,5)
Salida esperada
{'pares':[2,4], 'impares':[1,3,5]}
💡 Colecciones: diccionario con claves string y valores list """

class Analizador_numeros:
    def __init__(self):
        self.historial_Par = []
        self.historial_Impar = []

    def es_par(self, numero):
        if numero % 2 == 0:
           return True
        else:
           return False

    def Separar(self, *args):
        diccionario = {
            "pares": [],
            "impares": []
        }

        for i in args:
            if self.es_par(i):
                diccionario["pares"].append(i)
                self.historial_Par.append(i)
            else:
                diccionario["impares"].append(i)
                self.historial_Impar.append(i)

        return diccionario

    def cantidad_p_I(self):
        cantP = len(self.historial_Par)
        cantI = len(self.historial_Impar)

        return (cantP, cantI)

resultado = Analizador_numeros()
while True:
    print("\n === ANALIZADOR DE NÚMEROS ===")
    print("1. Clasificar un lote de números (Pares e Impares)")
    print("2. Ver cantidad total acumulada (Tupla)")
    print("3. Salir")

    opcion = input("Ingrese una opcion del menu (1-3): ")

    match opcion:
        case "1":
            entrada = input("Ingrese los numeros separados por espacio ( ) o por coma (,): ")
            numero_tex = entrada.replace(",", " ").split()
            lista_num = [int(i) for i in numero_tex]

            resultado_dic = resultado.Separar(*lista_num)
            print("Se registro con exito.")

        case "2":
            cantidad = resultado.cantidad_p_I()
            print(f"La cantidad por tipo es: {cantidad}")

        case "3":
            print("===CERRANDO PROGRAMA===")
            break

        case _:
            print("Opcion invalida.")


#EJERCICIO SIMILAR
"""CLASIFICADOR DE PRODUCTOS

Crear una clase llamada ClasificadorProductos que permita clasificar productos según su precio.

1. Método es_caro(precio)
Debe recibir un precio y retornar:

True si el precio es mayor o igual a 100.
False si el precio es menor a 100.

2. Método separar(*precios)
Debe recibir múltiples precios mediante *args y clasificarlos en un diccionario con las siguientes claves:

{
    "caros": [...],
    "baratos": [...]
}

Debe reutilizar el método es_caro() para determinar dónde colocar cada precio.

Ejemplo:

cp.separar(50, 120, 80, 200, 30)

Resultado:

{
    "caros": [120, 200],
    "baratos": [50, 80, 30]
}

3. Método cantidad_caros_baratos()
Debe retornar una tupla con la cantidad acumulada de productos caros y baratos:

(cantidad_caros, cantidad_baratos)

Entrada: múltiples precios en lote.
Proceso: clasificar los precios utilizando el operador de comparación y reutilizando es_caro().
Salida: diccionario con precios clasificados y tupla con cantidades acumuladas.

Colecciones utilizadas:

Diccionario con claves str y valores list.
Listas para almacenar el historial.
Tupla para retornar las cantidades.
*args para recibir múltiples precios."""

class ClasificadorProductos:
    def __init__(self):
        self.caro = []
        self.barato = []

    def es_caro(self, precio):
        if precio >= 100:
            return True
        else:
            return False

    def separar(self, *precios):
        diccionario = {
            "caros": [],
            "baratos": []
        }

        for i in precios:
            if self.es_caro(i):
                diccionario["caros"].append(i)
                self.caro.append(i)
            else:
                diccionario["baratos"].append(i)
                self.barato.append(i)

        return diccionario

    def cantidad_caros_baratos(self):
        cantb = len(self.barato)
        cantc = len(self.caro)

        return (cantc, cantb)


resultado = ClasificadorProductos()

while True:
    print("\n=== CLASIFICADOR DE PRODUCTOS ===")
    print("1. Clasificar precios")
    print("2. Ver cantidades acumuladas")
    print("3. Salir")

    opcion = input("Ingrese una opcion (1-3): ")

    match opcion:
        case "1":
            entrada = input("Ingrese los precios separados por espacio o coma: ")

            precios_texto = entrada.replace(",", " ").split()

            precios = [float(i) for i in precios_texto]

            resultado_dic = resultado.separar(*precios)

            print(f"Resultado: {resultado_dic}")

        case "2":
            cantidades = resultado.cantidad_caros_baratos()

            print(f"Cantidad de caros: {cantidades[0]}")
            print(f"Cantidad de baratos: {cantidades[1]}")

        case "3":
            print("=== CERRANDO PROGRAMA ===")
            break

        case _:
            print("Opcion invalida.")
