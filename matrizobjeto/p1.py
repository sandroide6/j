class Producto1:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad

def sumar_inventario():
    filas = int(input("Ingrese el número de filas: "))
    columnas = int(input("Ingrese el número de columnas: "))
    matriz = []
    
    for i in range(filas):
        fila = []
        for j in range(columnas):
            nombre = input(f"Ingrese nombre del producto en [{i}][{j}]: ")
            cantidad = int(input(f"Ingrese cantidad de {nombre}: "))
            fila.append(Producto1(nombre, cantidad))
        matriz.append(fila)
    
    total = 0
    for i in range(filas):
        for j in range(columnas):
            total += matriz[i][j].cantidad
    
    print("Inventario total:", total)