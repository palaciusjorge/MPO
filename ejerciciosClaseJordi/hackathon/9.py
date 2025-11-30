peliculas = []
while True:
    print("\n--- TU LISTA DE PELÍCULAS ---")
    print("1. Añadir película")
    print("2. Número total de películas")
    print("Escribe 'SALIR' para terminar")
    entrada = input("Selecciona una opción: ").strip().upper()
    match entrada:
        case 'SALIR':
            print("Te muestro como ha quedado tu lista de peliculas y cual fue la primera y ultima que mencionaste: ")
            break
        case "1":
            pelicula = input("Introduce la pelicula que quieres registrar: ").capitalize()
            peliculas.append(pelicula)
            print(f"Pelicula '{pelicula}' añadida correctamente.")
        case "2":
            print(f"Tu listado tiene un total de {len(peliculas)} peliculas.")
        case _:
            print("Opcion no valida")
if len(peliculas) > 0:  
    print(set(peliculas))
    print(f"La primera pelicula mencionada fue: {peliculas[0]}\nLa ultima pelicula mencionada fue: {peliculas[-1]}")
else:
    print("tu lista de peliculas esta vacia")
    

