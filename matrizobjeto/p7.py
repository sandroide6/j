class Producto:
    def __init__(self, nombre, peso, categoria):
        self.nombre = nombre
        self.peso = peso
        self.categoria = categoria

def organizar_estanterias():
    filas = int(input("Ingrese el número de filas: "))
    columnas = int(input("Ingrese el número de columnas: "))
    matriz = []
    categorias = {}
    
    for i in range(filas):
        fila = []
        for j in range(columnas):
            nombre = input(f"Ingrese nombre del producto en [{i}][{j}]: ")
            peso = float(input(f"Ingrese peso de {nombre}: "))
            categoria = input(f"Ingrese categoría de {nombre}: ")
            producto = Producto(nombre, peso, categoria)
            fila.append(producto)
            if categoria not in categorias:
                categorias[categoria] = []
            categorias[categoria].append(producto)
        matriz.append(fila)
    
    print("Productos organizados por categoría:")
    for clave, lista in categorias.items():
        print(f"{clave}: {[p.nombre for p in lista]}")