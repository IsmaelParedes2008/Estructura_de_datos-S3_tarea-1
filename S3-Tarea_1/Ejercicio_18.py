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

#EJERCICIO SIMILAR
"""Matriz de tiempos

Clase CalculadorTiempo que:

Tenga un método tiempo_transcurrido(p1, p2) que reciba dos tuplas (hora, minuto) y calcule los minutos transcurridos entre ambos horarios.
Tenga un método horario_mas_cercano(referencia, *horarios) que reciba un horario de referencia y varios horarios, y retorne el horario que tenga menor diferencia de tiempo con la referencia.
Tenga un atributo tipo lista para guardar todos los tiempos calculados.
Entrada

Tuplas (hora, minuto) como horarios.

Proceso
Convertir los horarios a minutos.
Calcular la diferencia.
Comparar las diferencias.
Guardar los resultados en la lista.
Salida
Tiempo transcurrido.
Horario más cercano."""

class CalculadorTiempo:
    def __init__(self):
        self.historial_tiempos = []

    def tiempo_transcurrido(self, p1, p2):
        h1, m1 = p1
        h2, m2 = p2

        tiempo = abs((h2 * 60 + m2) - (h1 * 60 + m1))

        self.historial_tiempos.append(tiempo)

        return tiempo

    def punto_mas_cercano(self, referencia, *horarios):
        if len(horarios) == 0:
            return None

        horario_cercano = None
        menor_tiempo = float('inf')

        for i in horarios:
            tiempo_actual = self.tiempo_transcurrido(referencia, i)

            if tiempo_actual < menor_tiempo:
                menor_tiempo = tiempo_actual
                horario_cercano = i

        return horario_cercano

resultado = CalculadorTiempo()

while True:
    print("\n=== CALCULADOR DE TIEMPOS ===")
    print("1. Calcular tiempo entre dos horarios")
    print("2. Buscar horario más cercano")
    print("3. Ver historial de tiempos")
    print("4. Salir")

    opcion = input("Ingrese una opción (1-4): ")

    match opcion:
        case "1":
            print("\n--- HORARIO 1 ---")
            h1 = int(input("Ingrese la hora: "))
            m1 = int(input("Ingrese los minutos: "))

            print("--- HORARIO 2 ---")
            h2 = int(input("Ingrese la hora: "))
            m2 = int(input("Ingrese los minutos: "))

            horario1 = (h1, m1)
            horario2 = (h2, m2)

            tiempo = resultado.tiempo_transcurrido(horario1, horario2)

            print(f"\nTiempo transcurrido: {tiempo} minutos")

        case "2":
            print("\n--- HORARIO DE REFERENCIA ---")
            h = int(input("Ingrese la hora: "))
            m = int(input("Ingrese los minutos: "))

            referencia = (h, m)

            n = int(input("\n¿Cuántos horarios desea comparar?: "))
            lista_horarios = []

            for i in range(n):
                print(f"\n--- Horario {i + 1} ---")
                hora = int(input("Ingrese la hora: "))
                minuto = int(input("Ingrese los minutos: "))

                lista_horarios.append((hora, minuto))

            cercano = resultado.horario_mas_cercano(
                referencia, *lista_horarios
            )

            print(f"\nEl horario más cercano es: {cercano}")

        case "3":
            print(f"\nHistorial de tiempos: {resultado.historial_tiempos}")

        case "4":
            print("=== CERRANDO EL PROGRAMA ===")
            break

        case _:
            print("Opción inválida.")
