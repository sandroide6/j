class Estudiante:
    def __init__(self, nombre,apellido,carnet,semestre,promedio,calificacion):
        self.nombre = nombre
        self.apellido= apellido
        self.carnet=carnet
        self.semestre=semestre
        self.promedio=promedio
        self.calificacion = calificacion

def agrupar_estudiantes():
    filas = int(input("Ingrese el número de filas: "))
    columnas = int(input("Ingrese el número de columnas: "))
    matriz = []
    
    for i in range(filas):
        fila = []
        for j in range(columnas):
            nombre = input(f"Ingrese nombre del estudiante en [{i}][{j}]: ")
            apellido= input(f"Ingrese nombre del estudiante en [{i}][{j}]: ")
            carnet= int(input(f"Ingrese el carnet del estudiante en [{i}][{j}]: "))
            semestre= int(input(f"Ingrese el semestre del estudiante en [{i}][{j}]: "))
            promedio= int(input(f"Ingrese nombre del estudiante en [{i}][{j}]: "))
            NumeroCalificaciones = int(input(f"Ingrese cuantas calificaciones tiene {nombre} (A, B, C, D, F): "))
            for w in range(NumeroCalificaciones):
                calificacion = input(f"Ingrese calificación de {nombre} (A, B, C, D, F): ")
            fila.append(Estudiante(nombre,apellido,carnet,semestre,promedio,calificacion))
        matriz.append(fila)
    

    




    grupo_EncimaDe4 = []
    grupo_DebajoDe4 = []
    grupo_Encima3 = []
    grupo_Debajo3 = []
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