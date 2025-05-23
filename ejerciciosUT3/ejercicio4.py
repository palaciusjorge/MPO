'''
Escribe un programa que pida al usuario dos listas de números enteros separados por comas y sume los elementos de ambas listas. 
El programa debe imprimir la lista resultante. Si las listas no tienen la misma longitud, el programa debe imprimir un mensaje de error.
'''
lista1 = input("Introduce la primera lista de numeros separados por comas: ").split(",")
lista2 = input("Introduce la segunda lista de numeros separados por comas: ").split(",")
if len(lista1) != len(lista2):
    print("Por favor introduce dos listas con la misma longitud")
else:
    listaSumatorio = []
    for i in range(len(lista2)):
        listaSumatorio.append(int(lista1[i]) + int(lista2[i]))
    print(f"La lista resultante de sumar las dos anteriores es : {listaSumatorio}")