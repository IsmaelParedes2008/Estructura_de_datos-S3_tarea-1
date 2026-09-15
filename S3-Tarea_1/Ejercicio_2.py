""" Contador de palabras únicas
Clase AnalizadorTexto que: (1) tenga método agregar_palabra(palabra) que agregue la palabra a un conjunto (para evitar duplicados) y a una lista (para el orden); 
(2) tenga método contar_palabras() que retorne cuántas palabras únicas hay; 
(3) tenga método agregar_multiples(*args) que reutilice agregar_palabra para varios.
Entrada
palabras individuales o en lotes
Proceso
guardar en conjunto y lista, contar únicas
Salida
cantidad de palabras únicas
Ejemplo de entrada
at = AnalizadorTexto()
at.agregar_multiples("hola","mundo","hola")
at.contar_palabras()
Salida esperada
2
💡 Colecciones: conjunto (para unicidad) + lista (para orden) """

class Analizador_Texto:
    def __init__(self):
        self.conjunto_palabras = set()
        self.lista_palabras = []

    def agregar_palabra(self, palabra):
        self.conjunto_palabras.add(palabra)
        self.lista_palabras.append(palabra)

    def contar_palabras(self):
        return len(self.conjunto_palabras)

    def agregar_multiples(self, *args):
        for i in args:
            self.agregar_palabra(i)

resultado = Analizador_Texto()
while True:
    print("\n ===MENU DEL ANALIZADOR DE TEXTO===")
    print("1. Agregar palabras")
    print("2. Contar palabras")
    print("3. Historial de palabras.")
    print("4. Salir")

    opcion = input("Ingrese una opcion (1-4): ")

    match opcion:
        case "1":
            entrada = input("Ingrese cada palabra separada por espacio( ) o por la coma(,): ")

            palabras_texto = entrada.replace(",", " ").split()

            resultado.agregar_multiples(*palabras_texto)
            print("Palabras ingresadas con exito.")

        case "2":
            conteo_palabras = resultado.contar_palabras()
            print(f"Total de palabras: {conteo_palabras}")

        case "3":
            print(f"Historial de palabras: {resultado.lista_palabras}")
            print(f"Sin duplicados: {resultado.conjunto_palabras}")

        case "4":
            print("===SALIENDO DEL PROGRAMA===")
            break

        case _:
            print("Opncion invalida")