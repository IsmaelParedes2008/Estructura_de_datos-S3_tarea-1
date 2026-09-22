""" Grupo de edades
Clase AgrupadorEdades que: 
(1) tenga método clasificar_edad(edad) que retorne la categoría ("niño", "adolescente", "adulto", "mayor"); 
(2) tenga método agrupar_por_categoria(*edades) que retorne un diccionario con {categoría: [edades]}; 
(3) tenga método edad_promedio_categoria(categoria).
Entrada
edades en lote
Proceso
clasificar con if/elif, agrupar en diccionario
Salida
diccionario agrupado, promedio
Ejemplo de entrada
ae = AgrupadorEdades()
ae.agrupar_por_categoria(5, 15, 30, 70)
Salida esperada
{'niño':[5], 'adolescente':[15], 'adulto':[30], 'mayor':[70]}
💡 Colecciones: diccionario de listas (estructura anidada) """

class AgrupadorEdades:
    def __init__(self):
        self.registro_etapas = {
            "niño": [],
            "adolescente": [],
            "adulto": [],
            "mayor": []
        }

    def clasificar_edad(self, edad):
        if edad < 12:
            return "niño"
        elif 12 <= edad < 18:
            return "adolescente"
        elif 18 <= edad < 60:
            return "adulto"
        else:
            return "mayor"

    def agrupar_por_categoria(self, *edades):
        dicc_lote = {"niño": [], "adolescente": [], "adulto": [], "mayor": []}
        
        for i in edades:
            categoria = self.clasificar_edad(i)
            dicc_lote[categoria].append(i)
            self.registro_etapas[categoria].append(i)
            
        return {k: v for k, v in dicc_lote.items() if v}

    def edad_promedio_categoria(self, categoria):
        lista_edades = self.registro_etapas.get(categoria, [])
        if len(lista_edades) == 0:
            return 0.0
        return sum(lista_edades) / len(lista_edades)


resultado = AgrupadorEdades()

while True:
    print("\n === MENU DEL AGRUPADOR DE EDADES ===")
    print("1. Registrar lote de edades (*args)")
    print("2. Ver edad promedio de una categoría")
    print("3. Ver todas las categorías agrupadas (Historial)")
    print("4. Salir")

    opcion = input("Ingrese una opción (1-4): ")

    match opcion:
        case "1":
            entrada = input("Ingrese las edades separadas por espacios o comas: ")
            texto = entrada.replace(",", " ").split()
            lista_edades = [int(i) for i in texto]
            
            resultado_diccionario = resultado.agrupar_por_categoria(*lista_edades)
            print(f"\nResultado del lote ingresado:\n{resultado_diccionario}")

        case "2":
            cat = input("¿Qué categoría desea consultar? (niño, adolescente, adulto, mayor): ").strip().lower()
            if cat in resultado.registro_etapas:
                prom = resultado.edad_promedio_categoria(cat)
                print(f"La edad promedio de la categoría '{cat}' es: {prom:.2f} años")
            else:
                print("Categoría inválida.")
                
        case "3":
            print(f"\nHistorial completo acumulado en la clase:\n{resultado.registro_etapas}")

        case "4":
            print("=== CERRANDO EL AGRUPADOR ===")
            break

        case _:
            print("Opción inválida. Intente de nuevo.")

#EJERCICIO SIMILAR
"""Agrupador de precios

Clase AgrupadorPrecios que:

Tenga un método clasificar_precio(precio) que retorne la categoría:
"barato" si el precio es menor a 20.
"medio" si está entre 20 y 99.
"caro" si es 100 o más.
Tenga un método agrupar_por_categoria(*precios) que reciba varios precios y retorne un diccionario con esta estructura:
{"barato": [precios], "medio": [precios], "caro": [precios]}
Tenga un método precio_promedio_categoria(categoria) que calcule el promedio de los precios registrados en una categoría.

Entrada: precios en lote.

Proceso: clasificar cada precio con if/elif y agruparlos en un diccionario de listas.

Salida: diccionario agrupado y promedio de una categoría."""

class AgrupadorPrecios:
    def __init__(self):
        self.registro_precios = {
            "barato": [],
            "medio": [],
            "caro": []
        }

    def clasificar_precio(self, precio):
        if precio < 20:
            return "barato"
        elif 20 <= precio < 100:
            return "medio"
        else:
            return "caro"

    def agrupar_por_categoria(self, *precios):
        dicc_lote = {
            "barato": [],
            "medio": [],
            "caro": []
        }

        for i in precios:
            categoria = self.clasificar_precio(i)
            dicc_lote[categoria].append(i)
            self.registro_precios[categoria].append(i)

        return {k: v for k, v in dicc_lote.items() if v}

    def precio_promedio_categoria(self, categoria):
        lista_precios = self.registro_precios.get(categoria, [])

        if len(lista_precios) == 0:
            return 0.0

        return sum(lista_precios) / len(lista_precios)

resultado = AgrupadorPrecios()

while True:
    print("\n=== MENU DEL AGRUPADOR DE PRECIOS ===")
    print("1. Registrar lote de precios")
    print("2. Ver precio promedio de una categoría")
    print("3. Ver todas las categorías agrupadas")
    print("4. Salir")

    opcion = input("Ingrese una opción (1-4): ")

    match opcion:
        case "1":
            entrada = input("Ingrese los precios separados por espacios o comas: ")

            texto = entrada.replace(",", " ").split()
            lista_precios = [float(i) for i in texto]

            resultado_diccionario = resultado.agrupar_por_categoria(*lista_precios)

            print(f"\nResultado del lote: {resultado_diccionario}")

        case "2":
            categoria = input(
                "Ingrese la categoría (barato, medio, caro): "
            ).strip().lower()

            if categoria in resultado.registro_precios:
                promedio = resultado.precio_promedio_categoria(categoria)
                print(f"Precio promedio: {promedio:.2f}")
            else:
                print("Categoría inválida.")

        case "3":
            print(f"\nHistorial completo: {resultado.registro_precios}")

        case "4":
            print("=== CERRANDO EL AGRUPADOR ===")
            break

        case _:
            print("Opción inválida.")
