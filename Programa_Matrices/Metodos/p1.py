import tkinter as tk
from tkinter import messagebox

class Producto1:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad

def sumar_inventario():
    def procesar_matriz():
        try:
            filas = int(entry_filas.get())
            columnas = int(entry_columnas.get())

            if filas <= 0 or columnas <= 0:
                messagebox.showerror("Error", "Las filas y columnas deben ser mayores a 0")
                return
            
            # Crear nueva ventana para ingresar productos
            ventana_productos = tk.Toplevel()
            ventana_productos.title("Ingresar Productos")

            matriz = []
            entries = []  # Guardar los campos de entrada
            
            def calcular_total():
                total = 0
                try:
                    for i in range(filas):
                        for j in range(columnas):
                            nombre = entries[i][j][0].get()
                            cantidad = int(entries[i][j][1].get())
                            matriz[i][j] = Producto1(nombre, cantidad)
                            total += cantidad
                    messagebox.showinfo("Inventario Total", f"Total de productos en inventario: {total}")
                    ventana_productos.destroy()  # Cerrar ventana después de procesar
                except ValueError:
                    messagebox.showerror("Error", "Ingrese valores numéricos válidos para la cantidad")
            
            for i in range(filas):
                fila = []
                matriz.append([None] * columnas)
                for j in range(columnas):
                    tk.Label(ventana_productos, text=f"Producto [{i}][{j}]:").grid(row=i*2, column=j, padx=5, pady=2)
                    entry_nombre = tk.Entry(ventana_productos, width=15)
                    entry_nombre.grid(row=i*2 + 1, column=j, padx=5, pady=2)
                    
                    entry_cantidad = tk.Entry(ventana_productos, width=5)
                    entry_cantidad.grid(row=i*2 + 2, column=j, padx=5, pady=2)

                    fila.append((entry_nombre, entry_cantidad))  # Guardar entradas
                entries.append(fila)

            tk.Button(ventana_productos, text="Calcular Total", command=calcular_total, bg="green", fg="white").grid(row=filas*2+1, columnspan=columnas, pady=10)

        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos")

    # Ventana principal para ingresar filas y columnas
    ventana = tk.Tk()
    ventana.title("Sumar Inventario")

    tk.Label(ventana, text="Ingrese el número de filas:").pack(pady=5)
    entry_filas = tk.Entry(ventana)
    entry_filas.pack(pady=5)

    tk.Label(ventana, text="Ingrese el número de columnas:").pack(pady=5)
    entry_columnas = tk.Entry(ventana)
    entry_columnas.pack(pady=5)

    tk.Button(ventana, text="Continuar", command=procesar_matriz, bg="blue", fg="white").pack(pady=10)

    ventana.mainloop()
