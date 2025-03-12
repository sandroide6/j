class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

def fusionar_matrices():
    filas = int(input("Ingrese el número de filas: "))
    columnas = int(input("Ingrese el número de columnas: "))
    matriz1 = []
    matriz2 = []
    matriz_resultante = []
    
    for i in range(filas):
        fila1 = []
        fila2 = []
        for j in range(columnas):
            nombre1 = input(f"Ingrese nombre del producto en [{i}][{j}] (Tienda 1): ")
            precio1 = float(input(f"Ingrese precio de {nombre1}: "))
            stock1 = int(input(f"Ingrese stock de {nombre1}: "))
            fila1.append(Producto(nombre1, precio1, stock1))
            
            nombre2 = input(f"Ingrese nombre del producto en [{i}][{j}] (Tienda 2): ")
            precio2 = float(input(f"Ingrese precio de {nombre2}: "))
            stock2 = int(input(f"Ingrese stock de {nombre2}: "))
            fila2.append(Producto(nombre2, precio2, stock2))
        
        matriz1.append(fila1)
        matriz2.append(fila2)




    
    for i in range(filas):
        fila_resultante = []
        for j in range(columnas):
            if matriz1[i][j].nombre == matriz2[i][j].nombre:
                nuevo_stock = matriz1[i][j].stock + matriz2[i][j].stock
                fila_resultante.append(Producto(matriz1[i][j].nombre, matriz1[i][j].precio, nuevo_stock))
            else:
                fila_resultante.append(matriz1[i][j])
                fila_resultante.append(matriz2[i][j])
        matriz_resultante.append(fila_resultante)
    
    print("Matriz resultante")
    for fila in matriz_resultante:
        for producto in fila:
            print(f"{producto.nombre}, Precio: {producto.precio}, Stock: {producto.stock}")
