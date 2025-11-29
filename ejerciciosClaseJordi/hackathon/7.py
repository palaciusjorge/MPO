"""
Analizador de texto
"""
frase = input("Introduce una frase: \n")
             
palabras = frase.split()
larger_word = palabras[0]
for p in palabras:
    if len(p) > len(larger_word):
        larger_word = p
print(f"La frase tiene un total de {len(frase)} caracteres, siendo la palabra mas larga: {larger_word} y teniendo un total de {len(palabras)} palabras")



