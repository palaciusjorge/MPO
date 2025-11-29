def analizar_lista(lista):
    if not lista:
        return {"error": "La lista está vacía"}

    analisis = {
        "maximo": max(lista),
        "minimo": min(lista),
        "media": sum(lista) / len(lista),
        "valores_unicos": list(set(lista))
    }

    return analisis
numeros = [5, 3, 9, 3, 5, 7, 9, 2]

resultado = analizar_lista(numeros)
print(resultado)