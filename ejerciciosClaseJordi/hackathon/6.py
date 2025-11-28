censored_words = ['tonto', 'feo', 'imbecil']

frase = input("Introduce cualquier frase: ")
palabras = frase.split()

nuevo_texto = [] 

for p in palabras:
    if p in censored_words:
        nuevo_texto.append('***')
    else:
        nuevo_texto.append(p)

nuevo_texto = " ".join(nuevo_texto)
print(nuevo_texto)