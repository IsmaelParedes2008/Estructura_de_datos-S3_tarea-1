""" Analizador de patrones en textos
Clase AnalizadorPatrones que: 
(1) tenga método encontrar_palabras(texto, patron) que busque palabras que inicien con el patrón y retorne una lista; 
(2) tenga método agrupar_por_longitud(texto) que retorne un diccionario {longitud: [palabras]}; 
(3) tenga método palabras_unicas() usando un conjunto.
Entrada
texto y patrón de búsqueda
Proceso
split(), filtrar, agrupar por longitud, eliminar duplicados
Salida
listas, diccionario, conjunto
Ejemplo de entrada
ap = AnalizadorPatrones()
ap.agrupar_por_longitud("el gato está aquí")
Salida esperada
{2:['el'], 4:['gato'], 5:['está'], 5:['aquí']}
💡 Colecciones: todas (lista, diccionario, conjunto) + métodos de string (split, startswith) """

class AnalizadorPatrones:
    def __init__(self):
        pass

    def encontrar_palabras(self, texto, patron):
        lista_coincidencias = []
        palabras = texto.split()
        for i in palabras:
            if i.startswith(patron):
                lista_coincidencias.append(i)
        return lista_coincidencias

    def agrupar_por_longitud(self, texto):
        diccionario_tamaños = {}
        palabras = texto.split()
        for i in palabras:
            largo = len(i)
            if largo in diccionario_tamaños:
                diccionario_tamaños[largo].append(i)
            else:
                diccionario_tamaños[largo] = [i]
        return diccionario_tamaños

    def palabras_unicas(self, texto):
        palabras = texto.split()
        conjunto_limpio = set(palabras)
        return conjunto_limpio

resultado = AnalizadorPatrones()

while True:
    print("\n === GESTOR DE PATRONES DE TEXTO ===")
    print("1. Buscar palabras que inicien con un patrón")
    print("2. Agrupar palabras por su longitud (Diccionario)")
    print("3. Ver palabras únicas (Conjunto sin repetidos)")
    print("4. Salir")

    opcion = input("Ingrese una opción (1-4): ")

    match opcion:
        case "1":
            frase = input("Ingrese el texto completo a analizar: ")
            patron = input("Ingrese las letras/patrón de búsqueda: ")
            coincidencias = resultado.encontrar_palabras(frase, patron)
            print(f"\nPalabras que inician con '{patron}': {coincidencias}")

        case "2":
            frase = input("Ingrese el texto completo para agrupar: ")
            dicc_resultado = resultado.agrupar_por_longitud(frase)
            print(f"\nDiccionario por longitudes resultante:\n{dicc_resultado}")

        case "3":
            frase = input("Ingrese el texto para extraer palabras únicas: ")
            conjunto_resultado = resultado.palabras_unicas(frase)
            print(f"\nConjunto de palabras únicas (sin repetir): {conjunto_resultado}")

        case "4":
            print("=== CERRANDO EL ANALIZADOR DE PATRONES ===")
            break

        case _:
            print("Opción inválida. Intente de nuevo.")
