'''
Escribe un programa que pida al usuario un número entero positivo e imprima la lista de divisores de ese número. Un divisor de un número n es un número entero que divide a n sin dejar residuo. El programa debe imprimir todos los divisores del número introducido.
'''
entero = int(input("Introduce un número entero: "))
lista = []
for i in range (entero):
    if entero % (i + 1) == 0:
        lista.append(i + 1)
    else:
        continue
print(f"La lista de divisores de {entero} es: {lista}")

