'''
Buscador de palabras
'''
import string

texto = input("Introduce el texto en el que quieras buscar una palabra concreta: \n").lower()
palabra = input("Introduce la palabra que quieras buscar: \n").lower()
texto = texto.translate(str.maketrans("", "", string.punctuation))
lista = texto.split()
contador = lista.count(palabra)
print(f"La palabra {palabra} aparece {contador} veces en el texto")

