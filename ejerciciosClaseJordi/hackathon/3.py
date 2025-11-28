nombre_completo = input("Introduce tu nombre completo: ")
palabras = nombre_completo.split()
iniciales = "".join([p[0].upper() for p in palabras])
print(f"Tus iniciales son: {iniciales}")


