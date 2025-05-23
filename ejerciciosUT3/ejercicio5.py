'''
Escribe un programa que pida al usuario una lista de números enteros separados por comas y la invierta. 
El programa debe imprimir la lista invertida.
'''
listaNumeros = input("Introduce la primera lista de numeros separados por espacios: ").split()
listaNumeros.reverse()
print(f"La lista al reves es : {listaNumeros}")
