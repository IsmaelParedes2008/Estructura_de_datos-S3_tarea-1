""" Matriz de distancias
Clase CalculadorDistancia que: 
(1) tenga método distancia_euclidiana(p1, p2) que reciba dos tuplas (x,y) y calcule la distancia; 
(2) tenga método punto_mas_cercano(referencia, *puntos) que retorne el punto más cercano a referencia; 
(3) tenga un atributo lista para guardar todas las distancias calculadas.
Entrada
tuplas (x, y) como puntos
Proceso
calcular distancia con fórmula, comparar, guardar
Salida
distancia numérica, punto más cercano
Ejemplo de entrada
cd = CalculadorDistancia()
cd.distancia_euclidiana((0,0), (3,4))
Salida esperada
5.0
💡 Colecciones: tuplas como puntos 2D; lista para guardar resultados """

class calculador_distancia:
    def __init__(self):
        self.historial_distancia = []

    def distancia_euclidiana(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        
        distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
        
        self.historial_distancia.append(distancia)
        
        return distancia        

    def punto_mas_cercano(self, referencia, *args):
        if len(args) == 0:
            return None
            
        punto_cercano = None
        min_distancia = float('inf')
        
        for i in args:
            distancia_actual = self.distancia_euclidiana(referencia, i)
    
            if distancia_actual < min_distancia:
                min_distancia = distancia_actual
                punto_cercano = i 
                
        return punto_cercano        

resultado = calculador_distancia()

while True:
    print("\n === GESTOR DE DISTANCIAS COORDENADAS ===")
    print("1. Calcular distancia entre dos puntos (Euclidiana)")
    print("2. Buscar el punto más cercano a una referencia (*args)")
    print("3. Ver historial de todas las distancias calculadas")
    print("4. Salir")

    opcion = input("Ingrese una opción (1-4): ")

    match opcion:
        case "1":
            print("\n--- PUNTO 1 ---")
            x1 = float(input("Ingrese coordenada X1: "))
            y1 = float(input("Ingrese coordenada Y1: "))
            
            print("--- PUNTO 2 ---")
            x2 = float(input("Ingrese coordenada X2: "))
            y2 = float(input("Ingrese coordenada Y2: "))
            
            dist_final = resultado.distancia_euclidiana((x1, y1), (x2, y2))
            print(f"\nLa distancia euclidiana resultante es: {dist_final:.2f}")

        case "2":
            print("\n--- PUNTO DE REFERENCIA ---")
            rx = float(input("Ingrese X de referencia: "))
            ry = float(input("Ingrese Y de referencia: "))
            referencia_tupla = (rx, ry)
            
            n = int(input("\n¿Cuántos puntos de destino desea evaluar?: "))
            lista_puntos = []
            
            for i in range(n):
                print(f"--- Punto {i+1} ---")
                px = float(input("Ingrese X: "))
                py = float(input("Ingrese Y: "))
                lista_puntos.append((px, py))
                
            top_cercano = resultado.punto_mas_cercano(referencia_tupla, *lista_puntos)
            print(f"\nEl punto más cercano a la referencia es: {top_cercano}")

        case "3":
            print(f"\nHistorial de todas las distancias registradas: {resultado.historial_distancia}")

        case "4":
            print("=== CERRANDO PROGRAMA ===")
            break

        case _:
            print("Opción inválida. Intente de nuevo.")