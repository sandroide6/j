class Asiento:
    def __init__(self, numero, fila, precio):
        self.numero = numero
        self.fila = fila
        self.precio = precio

def ordenar_asientos():
    filas = int(input("Ingrese el número de filas: "))
    columnas = int(input("Ingrese el número de columnas: "))
    matriz = []
    
    for i in range(filas):
        fila = []
        for j in range(columnas):
            numero = int(input(f"Ingrese número del asiento en [{i}][{j}]: "))
            precio = float(input(f"Ingrese precio del asiento {numero}: "))
            fila.append(Asiento(numero, i, precio))
        matriz.append(sorted(fila, key=lambda x: x.precio))
    
    print("Asientos ordenados por precio:")
    for i in range(filas):
        for asiento in matriz[i]:
            print(f"Fila {asiento.fila}, Asiento {asiento.numero}, Precio {asiento.precio}")
