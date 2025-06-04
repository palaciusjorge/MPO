'''
Escribe un programa que pida al usuario un texto y cuente cuántas veces aparece cada palabra en el texto.
El programa debe imprimir un diccionario donde las claves son las palabras y los valores son sus respectivas frecuencias.
Ignora la puntuación y considera las palabras en minúsculas.
'''
import string

texto = input("Introduce un texto: ")


texto = texto.lower()
texto = texto.translate(str.maketrans('', '', string.punctuation))

palabras = texto.split()

frecuencias = {}
for palabra in palabras:
    if palabra in frecuencias:
        frecuencias[palabra] += 1
    else:
        frecuencias[palabra] = 1

print(frecuencias)