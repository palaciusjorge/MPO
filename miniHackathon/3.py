'''
Clasificador de correos
'''
correos = input("Introduce una lista de correos separados por comas: \n")
lista_correos = correos.split(",")
lista_gmail = []
otros_correos = []
for correo in lista_correos:
    if correo.__contains__("@gmail"):
        lista_gmail.append(correo)
    else:
        otros_correos.append(correo)
print(f"La lista de correos de gmail es: {lista_gmail}.\nLa lista de otros dominios es: {otros_correos}")
