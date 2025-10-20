'''Escribe un programa que gestione un diccionario de productos, y por cada producto una lista de ventas diarias representadas como tuplas (día, unidades_vendidas). Haz un menú que permita al usuario:

Añadir un producto con su nombre.
Añadir un registro de ventas para un producto específico.
Consultar las ventas totales de un producto. El programa debe ejecutarse indefinidamente hasta que el usuario introduzca "SALIR".'''

productos = {}
while True:
    print("\n--- MENÚ DE INVENTARIO ---")
    print("1. Añadir producto")
    print("2. Registro de ventas")
    print("3. Consultar ventas de un producto")
    print("Escribe 'SALIR' para terminar")
    entrada = input("Selecciona una opción: ").strip().upper()
    if entrada == 'SALIR':
        print("Cerrando el programa.")
        break
    elif entrada == "1":
        producto = input("Introduce el producto que quieres registrar: ").strip().capitalize()
        productos[producto] = []
        print(f"Producto '{producto}' añadido correctamente.")
    elif entrada == '2':
        producto = input("Introduce el producto al que quieres añadir una venta: ").strip().capitalize()
        dia = input("Introduce el día de la venta (por ejemplo, Lunes): ").strip().capitalize()
        unidades = int(input("Introduce el numero de unidades vendidas: "))
        productos[producto].append((dia, unidades))
        print(f"Venta registrada: {unidades} unidades el {dia} para '{producto}'.")
    elif entrada == '3':
        producto = input("Introduce el producto que quieres consultar: ").strip().capitalize()
        ventas = productos[producto]
        if not ventas:
            print(f"No hay ventas registradas para '{producto}'.")
        else:
            total = sum(unidades for _, unidades in ventas)
            print(f"\nVentas de '{producto}':")
            for dia, unidades in ventas:
                print(f" - {dia}: {unidades} unidades")
            print(f"\n Total vendido: {total} unidades.")
    else:
        print("Opción no válida")
    



