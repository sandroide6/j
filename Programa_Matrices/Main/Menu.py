import tkinter as tk
import Metodos.p1 as p1
import Metodos.p2 as p2
import Metodos.p3 as p3
import Metodos.p4 as p4
import Metodos.p5 as p5
import Metodos.p6 as p6
import Metodos.p7 as p7
import Metodos.p8 as p8
import Metodos.p9 as p9
import Metodos.p10 as p10

def ejecutar_opcion(opcion):
    funciones = {
        1: p1.sumar_inventario,
        2: p2.libro_mas_caro,
        3: p3.ordenar_asientos,
        4: p4.fusionar_matrices,
        5: p5.filtrar_disponibles,
        6: p6.agrupar_estudiantes,
        7: p7.organizar_estanterias,
        8: p8.mejor_vendedor,
        9: p9.contar_ofertas,
        10: p10.buscar_producto
    }
    
    funcion = funciones.get(opcion)
    if funcion:
        funcion()

# Crear ventana
ventana = tk.Tk()
ventana.title("Ejercicios de Matrices")
ventana.geometry("400x500")

# Título
tk.Label(ventana, text="EJERCICIOS DE MATRICES", font=("Arial", 14, "bold")).pack(pady=10)

# Crear botones para cada opción
opciones = [
    ("Sumar Inventario", 1),
    ("Libro Más Caro", 2),
    ("Ordenar Asientos", 3),
    ("Fusionar Matrices", 4),
    ("Filtrar Disponibles", 5),
    ("Agrupar Estudiantes", 6),
    ("Organizar Estanterías", 7),
    ("Mejor Vendedor", 8),
    ("Contar Ofertas", 9),
    ("Buscar Producto", 10)
]

for texto, num in opciones:
    tk.Button(ventana, text=texto, font=("Arial", 12), width=25, height=1, command=lambda n=num: ejecutar_opcion(n)).pack(pady=5)

# Botón para salir
tk.Button(ventana, text="Salir", font=("Arial", 12, "bold"), bg="red", fg="white", width=25, command=ventana.quit).pack(pady=10)

# Iniciar la aplicación
ventana.mainloop()
