'''
Escribe un programa que pida al usuario una lista de palabras separadas por comas y cuente cuántas palabras hay en la lista.
El programa debe imprimir el resultado.
'''
miLista = input("Introduce una lista de palabras separadas por comas : ").split(",")
print(f"Has introducido una lista con {len(miLista)} palabras")