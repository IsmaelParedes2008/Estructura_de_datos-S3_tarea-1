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

        case _:
            print("Opcion invalida.")