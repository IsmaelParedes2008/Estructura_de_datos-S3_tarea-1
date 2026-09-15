
""" Validador de caracteres
Clase AnalizadorString que: 
(1) tenga método solo_vocales(letra) que retorne True si es vocal; 
(2) tenga método contar_por_tipo(texto) que retorne un 
diccionario {'vocales': cant, 'consonantes': cant, 'digitos': cant} reutilizando métodos; 
(3) tenga atributo que guarde el texto más largo analizado.
Entrada
textos para analizar
Proceso
recorrer carácter a carácter, clasificar
Salida
diccionario con conteos
Ejemplo de entrada
astr = AnalizadorString()
astr.contar_por_tipo("Hola123")
Salida esperada
{'vocales':2, 'consonantes':2, 'digitos':3}
💡 Colecciones: diccionario para contar tipos """

class Analizador_string:
    def __init__(self):
        self.caracter = ""

    def solo_vocales(self, vocal):
        if vocal in "AaEeIiOoUu":
            return True
        else:
            return False

    def contar_tipo(self, texto):
        if len(texto) > len(self.caracter):
            self.caracter = texto

        diccionario_conteo = {
                    'vocales': 0,
                    'consonantes': 0,
                    'digitos': 0
                }    

        for i in texto:
            if self.solo_vocales(i):
                diccionario_conteo['vocales'] += 1
            elif i.isdigit():
                diccionario_conteo['digitos'] += 1
            elif i.isalpha():
                diccionario_conteo['consonantes'] += 1
                
        return diccionario_conteo

resultado = Analizador_string()

while True:
    print("\n === MENU DEL ANALIZADOR DE TEXTO ===")
    print("1. Analizar una cadena de texto (frase o palabra)")
    print("2. Ver el texto más largo analizado")
    print("3. Salir")

    opcion = input("Ingrese una opción (1-3): ")

    match opcion:
        case "1":
            entrada = input("Ingrese el texto a analizar: ")
            
            diccionario_resultado = resultado.contar_tipo(entrada)
            print(f"\nResultado del conteo: {diccionario_resultado}")

        case "2":
            print(f"\nEl texto más largo analizado hasta ahora es: '{resultado.caracter}'")
            print(f"Total de caracteres del texto más largo: {len(resultado.caracter)}")

        case "3":
            print("=== CERRANDO PROGRAMA ===")
            break

        case _:
            print("Opción inválida. Intente de nuevo.")
        

    