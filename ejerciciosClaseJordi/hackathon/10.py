productos = {}

while True:
    print("\n--- MENÚ DE INVENTARIO ---")
    print("1. Añadir producto")
    print("2. Vender producto")
    print("3. Visualizar inventario")
    print("Escribe 'SALIR' para terminar")

    entrada = input("Selecciona una opción: ").strip().upper()

    match entrada:

        case 'SALIR':
            print("Cerrando el programa.")
            break

        case "1": 
            producto = input("Introduce el producto que quieres registrar: ").strip().capitalize()

            if producto in productos:
                print("Ese producto ya existe. Usa otra opción si deseas modificar su inventario.")
            else:
                try:
                    unidades = int(input("Introduce la cantidad inicial disponible: "))
                    productos[producto] = unidades
                    print(f"Producto '{producto}' añadido con {unidades} unidades.")
                except ValueError:
                    print("Debes introducir un número válido.")

        case "2": 
            producto = input("Introduce el producto que quieres vender: ").strip().capitalize()

            if producto not in productos:
                print("Ese producto no existe. Debes añadirlo primero.")
                continue

            try:
                unidades = int(input("¿Cuántas unidades se han vendido?: "))

                if unidades > productos[producto]:
                    print("No hay suficientes unidades disponibles.")
                else:
                    productos[producto] -= unidades
                    print(f"Venta realizada. Ahora quedan {productos[producto]} unidades de '{producto}'.")
            except ValueError:
                print("Debes introducir un número válido.")

        case "3": 
            if not productos:
                print("El inventario está vacío.")
            else:
                print("\n--- INVENTARIO ACTUAL ---")
                for producto, unidades in productos.items():
                    print(f"{producto}: {unidades} unidades disponibles")

        case _:
            print("Opción no válida.")