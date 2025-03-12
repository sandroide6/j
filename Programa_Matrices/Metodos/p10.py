class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

def buscar_producto():
    filas = int(input("Ingrese el número de filas: "))
    columnas = int(input("Ingrese el número de columnas: "))
    matriz = []
    
    for i in range(filas):
        fila = []
        for j in range(columnas):
            nombre = input(f"Ingrese nombre del producto en [{i}][{j}]: ")
            precio = float(input(f"Ingrese precio de {nombre}: "))
            fila.append(Producto(nombre, precio))
        matriz.append(fila)
    
    nombre_buscar = input("Ingrese el nombre del producto a buscar: ")
    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j].nombre == nombre_buscar:
                print("Producto encontrado en posición:", i, j)
                return
    print("Producto no encontrado")
