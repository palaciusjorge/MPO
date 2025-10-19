'''Escribe un programa que gestione un inventario de productos utilizando un diccionario. 
El programa debe permitir al usuario añadir productos con su nombre y cantidad, eliminar productos, y consultar la cantidad de un producto específico. 
El programa debe ejecutarse indefinidamente hasta que el usuario introduzca "SALIR".'''
inventario = {}

while True:
    print("\n--- MENÚ DE INVENTARIO ---")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Consultar producto")
    print("4. Mostrar todo el inventario")
    print("Escribe 'SALIR' para terminar")

    opcion = input("\nSelecciona una opción: ").strip().upper()

    if opcion == "SALIR":
        print("\nSaliendo del programa. ¡Hasta luego!")
        break

    elif opcion == "1":
        nombre = input("Nombre del producto: ").strip().capitalize()
        cantidad = input("Cantidad: ")

        if not cantidad.isdigit():
            print("Error: la cantidad debe ser un número entero.")
            continue

        cantidad = int(cantidad)
        inventario[nombre] = inventario.get(nombre, 0) + cantidad
        print(f"Producto '{nombre}' añadido con cantidad {cantidad} (Total: {inventario[nombre]}).")

    elif opcion == "2":
        nombre = input("Nombre del producto a eliminar: ").strip().capitalize()
        if nombre in inventario:
            del inventario[nombre]
            print(f"Producto '{nombre}' eliminado del inventario.")
        else:
            print(f"El producto '{nombre}' no existe en el inventario.")

    elif opcion == "3":
        nombre = input("Nombre del producto a consultar: ").strip().capitalize()
        if nombre in inventario:
            print(f"{nombre}: {inventario[nombre]} unidades.")
        else:
            print(f"El producto '{nombre}' no está en el inventario.")

    elif opcion == "4":
        if not inventario:
            print("El inventario está vacío.")
        else:
            print("\nInventario actual:")
            for producto, cantidad in inventario.items():
                print(f"   - {producto}: {cantidad}")

    else:
        print("Opción no válida. Inténtalo de nuevo.")
