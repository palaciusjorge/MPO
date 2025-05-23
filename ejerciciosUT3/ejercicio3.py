'''
Escribe un programa que pida al usuario una lista de números enteros separados por comas y encuentre el mayor y el menor elemento de la lista. 
El programa debe imprimir ambos resultados.
'''
miLista = input("Introduce una lista de numeros enteros separados por comas :").split(",")
for i in range(len(miLista)):
    miLista[i] = int(miLista[i])
miLista.sort()
print(f"El elemento mas pequeño de la lista es {miLista[0]} y el mas grande es {miLista[len(miLista) - 1]}.")
