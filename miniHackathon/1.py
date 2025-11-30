"""
Contador de palabras en una frase
"""
frase = input("Introduce una frase: ")
lista_palabras = frase.split()
print(f"La frase tiene: {len(lista_palabras)} palabras.\nLa primera palabra es: {lista_palabras[0]}.\nLa ultima palabra es: {lista_palabras[-1]}.")
