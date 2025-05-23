'''
Escribe un programa que pida al usuario una lista de números enteros separados por comas y calcule la suma de todos los elementos de la lista.
El programa debe imprimir el resultado.
'''
miLista = input("Introduce una lista de numeros enteros separados por comas :").split(",")
listaNumeros = []
sumatorio = 0
for i in range(len(miLista)):
    listaNumeros.append(int(miLista[i]))
    sumatorio += int(miLista[i])
print(f"El sumatorio de la lista {listaNumeros} es {sumatorio}")