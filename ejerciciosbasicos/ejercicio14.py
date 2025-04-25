'''
Escribe un programa que pida al usuario un número entero positivo e imprima la suma de los números pares por un lado y la suma de los números impares por otro. El programa debe imprimir ambos resultados.
'''
entero = int(input("Introduce un número entero :"))
suma_par = 0
suma_impar = 0
for i in range (entero + 1):
    if i % 2 == 0:
        suma_par += i
    else:
        suma_impar += i

print(f"El sumatorio de los números pares es: {suma_par} y el de los impares es: {suma_impar}")
