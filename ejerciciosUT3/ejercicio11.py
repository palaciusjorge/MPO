'''Escribe un programa que gestione una biblioteca digital utilizando un diccionario.
El programa debe permitir al usuario añadir libros con su título, autor y año de publicación. 
El usuario debe poder consultar los libros por autor o por año de publicación. 
El programa debe ejecutarse indefinidamente hasta que el usuario introduzca "SALIR".'''
biblioteca = {}
while True:
    print("\n--- MENÚ DE INVENTARIO ---")
    print("1. Añadir libro")
    print("2. Consultar libro por autor")
    print("3. Consultar libro por año de publicación")
    print("Escribe 'SALIR' para terminar")
    opcion = input("\nSelecciona una opción: ").strip().upper()
    if opcion == 'SALIR':
        print("\nSaliendo del programa. ¡Hasta luego!")
        break
    elif opcion == "1":
        nombre = input("Nombre del libro: ").strip().capitalize()
        autor = input("Autor: ").strip().capitalize()
        publicacion = int(input("Año de publicación: "))

        biblioteca[nombre] = {"autor": autor, "publicacion": publicacion}

        print(f"Se ha añadido el libro '{nombre}' de {autor}, publicado en {publicacion}.")
    elif opcion == "2":
        autor_buscar = input("Introduce el autor: ").strip().capitalize()
        encontrados = [titulo for titulo, datos in biblioteca.items() if datos["autor"] == autor_buscar]

        if encontrados:
            print(f"\n Libros de {autor_buscar}:")
            for titulo in encontrados:
                print(f" - {titulo} ({biblioteca[titulo]['publicacion']})")
        else:
            print(f" No se encontraron libros de {autor_buscar}.")
    elif opcion == "3":
        publicacion_buscar = input("Introduce el año de publicación: ").strip()
        encontrados = [titulo for titulo, datos in biblioteca.items() if str(datos["publicacion"]) == publicacion_buscar]
        if encontrados:
            print(f"\n Libros publicados en {publicacion_buscar}:")
            for titulo in encontrados:
                print(f" - {titulo} (Autor: {biblioteca[titulo]['autor']})")
        else:
            print(f" No se encontraron libros del año {publicacion_buscar}.")

    else:
        print("Opción no válida. Intenta de nuevo.")




    