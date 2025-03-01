import p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,prueba

while True:
    try:
        print("\nEjercicios de Matrices")
        print("1. sumar_inventario")
        print("2. libro_mas_caro")
        print("3. ordenar_asientos")
        print("4. fusionar_matrices")
        print("5. filtrar_disponibles")
        print("6. agrupar_estudiantes")
        print("7. organizar_estanterias")
        print("8. mejor_vendedor")
        print("9. contar_ofertas")
        print("10. buscar_producto")
        print("0. Salir")
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 0:
            break
        elif opcion == 1:
            p1.sumar_inventario()
        elif opcion == 2:
            p2.libro_mas_caro()
        elif opcion == 3:
            p3.ordenar_asientos()
        elif opcion == 4:
            prueba.fusionar_matricess()
        elif opcion == 5:
            p5.filtrar_disponibles()
        elif opcion == 6:
            p6.agrupar_estudiantes()
        elif opcion == 7:
            p7.organizar_estanterias()
        elif opcion == 8:
            p8.mejor_vendedor()
        elif opcion == 9:
            p9.contar_ofertas()
        elif opcion == 10:
            p10.buscar_producto()
    except ValueError:
        print("Ingrese un numero valido")
        
