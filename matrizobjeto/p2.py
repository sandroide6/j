class Libro:
    def __init__(self, titulo, autor, precio):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio

def libro_mas_caro():
    filas = int(input("Ingrese el número de filas: "))
    columnas = int(input("Ingrese el número de columnas: "))
    matriz = []
    
    for i in range(filas):
        fila = []
        for j in range(columnas):
            titulo = input(f"Ingrese título del libro en [{i}][{j}]: ")
            autor = input(f"Ingrese autor de {titulo}: ")
            precio = float(input(f"Ingrese precio de {titulo}: "))
            fila.append(Libro(titulo, autor, precio))
        matriz.append(fila)
    
    mas_caro = matriz[0][0]
    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j].precio > mas_caro.precio:
                mas_caro = matriz[i][j]
    
    print("El libro más caro es:", mas_caro.titulo, "de", mas_caro.autor, "con precio de", mas_caro.precio)