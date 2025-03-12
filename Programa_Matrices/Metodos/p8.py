class Vendedor:
    def __init__(self, nombre, ventas):
        self.nombre = nombre
        self.ventas = ventas

def mejor_vendedor():
    filas = 5
    columnas = 12
    matriz = []
    mejor = None
    
    for i in range(filas):
        nombre = input(f"Ingrese el nombre del vendedor {i + 1}: ")
        ventas = []
        total = 0
        for j in range(columnas):
            venta = float(input(f"Ingrese ventas del mes {j + 1} para {nombre}: "))
            ventas.append(venta)
            total += venta
        matriz.append(Vendedor(nombre, total))
        if mejor is None or total > mejor.ventas:
            mejor = matriz[-1]
    
    print("El mejor vendedor es:", mejor.nombre, "con ventas de", mejor.ventas)