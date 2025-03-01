class Estudiante:
    def __init__(self, nombre, calificacion):
        self.nombre = nombre
        self.calificacion = calificacion

def agrupar_estudiantes():
    filas = int(input("Ingrese el número de filas: "))
    columnas = int(input("Ingrese el número de columnas: "))
    matriz = []
    
    for i in range(filas):
        fila = []
        for j in range(columnas):
            nombre = input(f"Ingrese nombre del estudiante en [{i}][{j}]: ")
            calificacion = input(f"Ingrese calificación de {nombre} (A, B, C, D, F): ")
            fila.append(Estudiante(nombre, calificacion))
        matriz.append(fila)
    
    grupo_A = []
    grupo_B = []
    grupo_C = []
    grupo_D = []
    grupo_F = []
    
    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j].calificacion == "A":
                grupo_A.append(matriz[i][j])
            elif matriz[i][j].calificacion == "B":
                grupo_B.append(matriz[i][j])
            elif matriz[i][j].calificacion == "C":
                grupo_C.append(matriz[i][j])
            elif matriz[i][j].calificacion == "D":
                grupo_D.append(matriz[i][j])
            else:
                grupo_F.append(matriz[i][j])
    
    print("Grupo A:")
    for estudiante in grupo_A:
        print(estudiante.nombre)
    print("Grupo B:")
    for estudiante in grupo_B:
        print(estudiante.nombre)
    print("Grupo C:")
    for estudiante in grupo_C:
        print(estudiante.nombre)
    print("Grupo D:")
    for estudiante in grupo_D:
        print(estudiante.nombre)
    print("Grupo F:")
    for estudiante in grupo_F:
        print(estudiante.nombre)