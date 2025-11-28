entrada = input("Introduce una lista de palabras separadas por comas: ")

palabras = [p.strip() for p in entrada.split(",")]


sin_duplicados = {}
for p in palabras:
    clave = p.lower()
    if clave not in sin_duplicados:
        sin_duplicados[clave] = p


resultado = sorted(sin_duplicados.values(), key=str.lower)

print(resultado)

