""" Clase CodificadorCesar que: 
(1) tenga método codificar_letra(letra, desplazamiento) que retorne la letra 
desplazada en el alfabeto (usar operador %); 
(2) tenga método codificar_palabra(palabra, desplazamiento) que reutilice para toda la palabra; 
(3) tenga un diccionario como atributo para historial de codificaciones.
Entrada
letra/palabra y desplazamiento (1-25)
Proceso
convertir a código ASCII, desplazar con %, guardar historial
Salida
palabra codificada
Ejemplo de entrada
cc = CodificadorCesar()
cc.codificar_palabra("hola", 3)
Salida esperada
"kroc" (aprox, solo ejemplo)
💡 Colecciones: diccionario para historial; ord() y chr() para conversión """


class CodificadorCesar:
    def __init__(self):
        self.cifrado_cesar = {}

    def codificar_letra(self, letra, desplazamiento):
        if "a" <= letra <= "z":
            posicion_original = ord(letra) - 97
            nueva_posicion = (posicion_original + desplazamiento) % 26
            return chr(nueva_posicion + 97)
        return letra

    def codificar_palabra(self, palabra, desplazamiento):
        mensaje_cifrado = ""
        mensaje_limpio = palabra.lower()
        
        for i in mensaje_limpio:
            mensaje_cifrado += self.codificar_letra(i, desplazamiento)
            
        self.cifrado_cesar[palabra] = mensaje_cifrado
        return mensaje_cifrado


resultado = CodificadorCesar()

while True:
    print("\n === MENU DEL CODIFICADOR CESAR ===")
    print("1. Codificar una palabra o frase")
    print("2. Ver historial de codificaciones (Diccionario)")
    print("3. Salir")

    opcion = input("Ingrese una opción (1-3): ")

    match opcion:
        case "1":
            entrada = input("Ingrese la palabra o mensaje a cifrar: ")
            salto = int(input("Ingrese el desplazamiento (1-25): "))
            
            palabra_encriptada = resultado.codificar_palabra(entrada, salto)
            print(f"\nTexto codificado final: '{palabra_encriptada}'")

        case "2":
            print(f"\nHistorial de codificaciones acumulado: {resultado.cifrado_cesar}")

        case "3":
            print("=== CERRANDO PROGRAMA ===")
            break

        case _:
            print("Opción inválida. Intente de nuevo.")

#EJERCICIO SIMILAR
"""Codificador de números
Clase CodificadorNumeros que:
Tenga un método codificar_numero(numero, desplazamiento) que retorne el número desplazado utilizando el operador %.
Tenga un método codificar_lista(lista, desplazamiento) que reutilice codificar_numero() para codificar todos los números de una lista.
Tenga un diccionario como atributo para guardar un historial de las codificaciones realizadas.

Entrada:
Número/lista de números y desplazamiento.

Proceso:
Desplazar cada número utilizando % y guardar el resultado en el historial.

Salida:
Lista de números codificados."""

class CodificadorNumeros:
    def __init__(self):
        self.historial = {}

    def codificar_numero(self, numero, desplazamiento):
        nuevo_numero = (numero + desplazamiento) % 100
        return nuevo_numero

    def codificar_lista(self, lista, desplazamiento):
        lista_codificada = []

        for i in lista:
            nuevo = self.codificar_numero(i, desplazamiento)
            lista_codificada.append(nuevo)

        self.historial[str(lista)] = lista_codificada

        return lista_codificada

resultado = CodificadorNumeros()

while True:
    print("\n=== MENU DEL CODIFICADOR DE NUMEROS ===")
    print("1. Codificar una lista")
    print("2. Ver historial de codificaciones")
    print("3. Salir")

    opcion = input("Ingrese una opción (1-3): ")

    match opcion:
        case "1":
            entrada = input("Ingrese los números separados por espacios o comas: ")
            
            texto = entrada.replace(",", " ").split()
            lista = [int(i) for i in texto]

            desplazamiento = int(input("Ingrese el desplazamiento: "))

            resultado_codificado = resultado.codificar_lista(lista, desplazamiento)

            print(f"\nLista codificada: {resultado_codificado}")

        case "2":
            print(f"\nHistorial: {resultado.historial}")

        case "3":
            print("=== CERRANDO PROGRAMA ===")
            break

        case _:
            print("Opción inválida.")
