""" Estadísticas de temperatura
Clase GestorTemperatura que: (1) tenga método registrar_temperatura(temp) que guarde en una lista; 
(2) tenga método minima()`, `maxima()`, `promedio() que calculen estadísticas; 
(3) tenga método registrar_multiples(*temps) que reutilice el registro para varias temperaturas.
Entrada
temperaturas individuales o en lote
Proceso
guardar, calcular mín, máx, promedio
Salida
valores estadísticos
Ejemplo de entrada
gt = GestorTemperatura()
gt.registrar_multiples(20,25,18,30)
gt.promedio()
Salida esperada
23.25
💡 Colecciones: lista de números + funciones built-in min/max """

class Gestor_Temperatura:
    def __init__(self):
        self.historial_temperatura = []

    def Registrar_temperatura(self, temperatura):
        self.historial_temperatura.append(temperatura)

    def registrar_varias(self, *args):
        for i in args:
            self.Registrar_temperatura(i)

    def temperatura_min(self):
        if len(self.historial_temperatura) == 0:
            return 0
        return min(self.historial_temperatura)

    def temperatura_max(self):
        if len(self.historial_temperatura)==0:
            return 0
        return max(self.historial_temperatura)

    def promedio_temperatura(self):
        if len(self.historial_temperatura) == 0:
            return 0.0
        return sum(self.historial_temperatura)/len(self.historial_temperatura)

resultado = Gestor_Temperatura()
while True:
    print("1. Registrar lote de temperaturas.")
    print("2. Ver estadísticas (Mínima, Máxima, Promedio).")
    print("3. Ver historial de temperaturas.")
    print("4. Salir.")

    opcion = input("Ingrese una opción (1-4): ")

    match opcion:
        case "1":
            entrada = input("Ingrese las temperaturas separadas por espacio ( ) o por coma(,): ")
            temperatura_tex = entrada.replace(",", " ").split()

            temperatura = [float(i) for i in temperatura_tex]
            resultado.registrar_varias(*temperatura)

            print("Registro exitoso.")

        case "2":
            print(f"A. Temperatura minima. {resultado.temperatura_min()}")
            print(f"B. Temperatura maxima. {resultado.temperatura_max()}")
            print(f"C. Temperatura promedio. {resultado.promedio_temperatura():.2f}")

        case "3":
            print(f"Historial de temperatura: {resultado.historial_temperatura}")

        case "4":
            print("===CERRANDO PROGRAMa===")
            break
        
        case _:
            print("Opcion invalida.")


#EJERCICIO SIMILAR
"""### ENUNCIADO

Crear una clase `Gestor_Ventas` que permita:

1. Registrar una venta y varias ventas usando `*args`.
2. Obtener las ventas mayores a un límite.
3. Calcular el total y la cantidad de ventas.
4. Mostrar los resultados mediante un menú.

**Ejemplo:**
Ventas: `50, 200, 80, 500`
Límite: `100`
Resultado: `[200, 500]`

### CÓDIGO

```python"""

class Gestor_Ventas:
    def __init__(self):
        self.ventas = []

    def registrar_venta(self, venta):
        self.ventas.append(venta)

    def registrar_varias(self, *args):
        for i in args:
            self.registrar_venta(i)

    def ventas_mayores(self, limite):
        lista = []
        for i in self.ventas:
            if i > limite:
                lista.append(i)
        return lista

    def total_ventas(self):
        return sum(self.ventas)

    def cantidad_ventas(self):
        return len(self.ventas)


resultado = Gestor_Ventas()

while True:
    print("\n=== GESTOR DE VENTAS ===")
    print("1. Registrar ventas")
    print("2. Ventas mayores a un límite")
    print("3. Total de ventas")
    print("4. Cantidad de ventas")
    print("5. Ver historial")
    print("6. Salir")

    opcion = input("Opción: ")

    match opcion:
        case "1":
            entrada = input("Ingrese ventas separadas por espacio o coma: ")
            ventas = [float(i) for i in entrada.replace(",", " ").split()]
            resultado.registrar_varias(*ventas)

        case "2":
            limite = float(input("Ingrese el límite: "))
            print(resultado.ventas_mayores(limite))

        case "3":
            print(f"Total: {resultado.total_ventas()}")

        case "4":
            print(f"Cantidad: {resultado.cantidad_ventas()}")

        case "5":
            print(f"Historial: {resultado.ventas}")

        case "6":
            break

        case _:
            print("Opción inválida.")
```


