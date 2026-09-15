""" Selector de rango con tuplas
Clase SelectorRango que: 
(1) tenga método crear_rango(inicio, fin) que retorne una tupla con números en ese rango; 
(2) tenga método elementos_en_multiples_rangos(*rangos) que reciba múltiples tuplas (inicio,fin) y retorne una 
lista combinada sin duplicados usando un conjunto.
Entrada
pares (inicio, fin) para varios rangos
Proceso
crear rangos como tuplas, unir sin duplicados
Salida
lista de elementos únicos
Ejemplo de entrada
sr = SelectorRango()
sr.elementos_en_multiples_rangos((1,3), (2,4))
Salida esperada
[1, 2, 3, 4]
💡 Colecciones: tuplas como parámetros + conjuntos para eliminar duplicados """

class Selector_rango:
    def __init__(self):
        pass

    def crear_rango(self, inicio, fin):
        lista = []
            
        for i in range(inicio, fin + 1):
            lista.append(i)
                    
        return tuple(lista)

  #  def crear_multiples_rangos(self, *lista_rangos):
  #      lista_de_tuplas_generadas = []
  #      
  #      for i in lista_rangos:
  #          inicio = i[0]
  #          fin = i[1]
  #          
  #          rango_tupla = self.crear_rango(inicio, fin)
  #          
  #          lista_de_tuplas_generadas.append(rango_tupla)
  #          
  #      return lista_de_tuplas_generadas

    def multiples_elementos(self, *lista_elementos):
        conjunto_limpio = set()

        for i in lista_elementos:
            inicio = i[0]
            fin = i[1]
                    
            elementos_tupla = self.crear_rango(inicio, fin)
                    
            for j in elementos_tupla:
                conjunto_limpio.add(j)
                        
        return sorted(list(conjunto_limpio))
        
resultado = Selector_rango()

while True:
    print("\n === SELECTOR DE RANGO ===")
    print("1. Crear un solo rango de números (Tupla)")
    print("2. Combinar múltiples rangos (*args)")
    print("3. Salir")

    opcion = input("Ingrese una opción (1-3): ")

    match opcion:
        case "1":
            ini = int(input("Ingrese el número de inicio: "))
            fin = int(input("Ingrese el número de fin: "))
            
            rango_tupla = resultado.crear_rango(ini, fin)
            print(f"\nTupla de números generada: {rango_tupla}")

        case "2":
            n = int(input("¿Cuántos rangos desea combinar?: "))
            lista_de_tuplas = []
            
            for i in range(n):
                print(f"\n--- Rango {i+1} ---")
                ini = int(input("Ingrese el número de inicio: "))
                fin = int(input("Ingrese el número de fin: "))
                # Guardamos como una tupla (ini, fin) dentro de la lista grande
                lista_de_tuplas.append((ini, fin))
                
            resultado_combinado = resultado.multiples_elementos(*lista_de_tuplas)
            print(f"\nLista de elementos únicos combinados: {resultado_combinado}")

        case "3":
            print("=== CERRANDO PROGRAMA ===")
            break

        case _:
            print("Opción inválida. Intente de nuevo.")










































# case "1":
#            print("\n--- CREACIÓN DE RANGOS ---")
#            print("A. Crear un solo rango de números")
#            print("B. Crear múltiples rangos de números")
#            sub_opcion = input("Elija una opción (A/B): ").upper()
#
#            if sub_opcion == "A":
#                ini = int(input("Ingrese el número de inicio: "))
#                fin = int(input("Ingrese el número de fin: "))
#                
#                rango_tupla = resultado.crear_rango(ini, fin)
#                print(f"\nTupla de números generada: {rango_tupla}")
#
#            elif sub_opcion == "B":
#                n = int(input("¿Cuántos rangos independientes desea crear?: "))
#                lista_de_pedidos = []
#                
#                for i in range(n):
#                    print(f"\n--- Rango {i+1} ---")
#                    ini = int(input("Ingrese el número de inicio: "))
#                    fin = int(input("Ingrese the número de fin: "))
#                    # Guardamos los límites como tupla temporal
#                    lista_de_pedidos.append((ini, fin))
#                
#                # Desarmamos con '*' para que entre al *args del nuevo método
#                resultado_lotes = resultado.crear_multiples_rangos(*lista_de_pedidos)
#                print(f"\nLista de rangos generados independientemente: {resultado_lotes}")
#            else:
#                print("Opción inválida.")













