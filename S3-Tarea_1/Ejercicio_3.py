""" EJERCICIO 3
Gestor de compras con totales
Clase CarroCompras que: (1) tenga método agregar_articulo(nombre, precio) que guarde en un 
diccionario {nombre: precio}; 
(2) tenga método total_carrito() que retorne la suma de todos los precios; 
(3) tenga método articulos_por_rango(precio_min, precio_max) que retorne una lista 
con artículos dentro del rango.
Entrada
nombres de artículos y precios
Proceso
guardar en diccionario, sumar valores, filtrar por rango
Salida
total, artículos en rango
Ejemplo de entrada
c = CarroCompras()
c.agregar_articulo("pan",2.50)
c.agregar_articulo("leche",3.00)
c.total_carrito()
Salida esperada
5.50
💡 Colecciones: diccionario para almacenar nombre→precio """

class Carro_compra:
    def __init__(self):
        self.carrito_diccionario = {}

    def Agregar_articulo(self, nombre, precio):
        self.carrito_diccionario[nombre] = precio

    def agregar_multiples(self, lista_articulos):
        for i in lista_articulos:

            partes = i.split(":")
            
            if len(partes) == 2:
                nombre = partes[0]
                precio = float(partes[1])
                
                self.Agregar_articulo(nombre, precio)


    def Total_carrito(self):
        sum = 0

        for i in self.carrito_diccionario.values():
            sum += i

        return sum

    def Articulo_rango(self, precioMi, precioMa):
        lista = []


        for nombre, precio in self.carrito_diccionario.items():
            if precioMi <= precio <= precioMa:
                lista.append(nombre)

        return lista

resultado = Carro_compra()
while True:
    print("\n ===MENU DEl CARRO DE COMPRA===")
    print("1. Registrar productos.")
    print("2. Suma total de productos.")
    print("3. Filtrar artículos por rango de precio.")
    print("4. Ver carrito completo.")
    print("5. Salir")

    opcion = input("Ingrese una opcion del menu (1-5): ")

    match opcion:

        case "1":
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            resultado.Agregar_articulo(nombre, precio)
            print(f"¡Se realizó con éxito el registro de {nombre}!")

   #     case "1":
   #         print("\n--- REGISTRO DE PRODUCTOS ---")
   #         print("A. Registrar un solo producto")
   #         print("B. Registrar lote de productos")
   #         sub_opcion = input("Elija una opción (A/B): ").upper()
#
   #         if sub_opcion == "A":
   #             nombre = input("Ingrese el nombre del producto: ")
   #             precio = float(input("Ingrese el precio del producto: "))
   #             resultado.Agregar_articulo(nombre, precio)
   #             print(f"¡Se realizó con éxito el registro de {nombre}!")
#
   #         elif sub_opcion == "B":
   #             entrada = input("Ingrese los productos en formato nombre:precio separados por espacios\n(Ejemplo: pan:2.50 leche:3.00 queso:4.00):\n> ")
   #             
   #             lote_texto = entrada.split()
   #         
   #             resultado.agregar_multiples(lote_texto)
   #             print("¡Lote de productos registrado con éxito!")
   #         
   #         else:
   #             print("Opción inválida.")
#

        case "2":
            total = resultado.Total_carrito()
            print(f"El valor total del carrito es: ${total}")

        case "3":
            precioMi = int(input("Ingrese el percio minimo a filtrar: "))
            precioMa = int(input("Ingrese el precio maximo a filtrar: "))

            resultado_rango = resultado.Articulo_rango(precioMi, precioMa)
            print(f"Productos en ese rango de precio: {resultado_rango}")

        case "4":
            print(f"Carrito de compra completo: {resultado.carrito_diccionario}")

        case "5":
            print("===CERRANDO PROGRAMA===")
            break

        case _:
            print("Opcion invalida.")