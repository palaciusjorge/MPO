'''
Palabra invertida
'''
palabra = input("Introduce la palabra que quieres dar la vuelta: ")
reverse = palabra[::-1].lower()
vocales = ["a", "e", "i", "o", "u"]
censurada = ''
for l in reverse:
    if l in vocales:
        censurada += "*"
    else:
        censurada += l
print(reverse)
print(censurada)