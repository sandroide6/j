class Producto:
    def __init__(self, nombre, oferta):
        self.nombre = nombre
        self.oferta = oferta

def contar_ofertas():
    n = int(input("Ingrese el tamaño de la matriz: "))
    matriz = []
    ofertas = 0
    
    for i in range(n):
        fila = []
        for j in range(n):
            nombre = input(f"Ingrese nombre del producto en [{i}][{j}]: ")
            oferta = input(f"¿Está en oferta? (si/no): ") == "si"
            fila.append(Producto(nombre, oferta))
            if oferta:
                ofertas += 1
        matriz.append(fila)
    
    print("Total de productos en oferta:", ofertas)