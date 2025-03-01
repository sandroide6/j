class Producto:
    def __init__(self, nombre, precio, disponible):
        self.nombre = nombre
        self.precio = precio
        self.disponible = disponible

def filtrar_disponibles():
    filas = int(input("Ingrese el número de filas: "))
    columnas = int(input("Ingrese el número de columnas: "))
    matriz = []
    nueva_matriz = []
    
    for i in range(filas):
        fila = []
        for j in range(columnas):
            nombre = input(f"Ingrese nombre del producto en [{i}][{j}]: ")
            precio = float(input(f"Ingrese precio de {nombre}: "))
            disponible = input(f"Está disponible? (si/no): ") == "si"
            fila.append(Producto(nombre, precio, disponible))
        matriz.append(fila)
    
    for i in range(filas):
        fila_nueva = []
        for j in range(columnas):
            if matriz[i][j].disponible:
                fila_nueva.append(matriz[i][j])
        if fila_nueva:
            nueva_matriz.append(fila_nueva)
    
    print("Productos disponibles:")
    for fila in nueva_matriz:
        for producto in fila:
            print(producto.nombre, producto.precio)