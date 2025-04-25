'''
Escribe un programa que pida al usuario un número entero positivo y calcules la suma de la potencia de 3 de cada número desde 1 hasta el número introducido. El programa debe imprimir el resultado.

Para que se entienda mejor, si el usuario introduce 3, el programa debe calcular:
'''
entero = int(input("Introduce un número entero :"))
suma = 0
for i in range(entero + 1):
    suma += i**3
print(f"La suma de las potencias de 3 desde 1 hasta {entero} es {suma}")
