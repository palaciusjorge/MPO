'''
Escribe un programa que pida al usuario dos números enteros e imprima la secuencia de números entre ellos (incluidos) en orden ascendente. Si el primer número es mayor que el segundo, imprime la secuencia en orden descendente. Debes imprimir la secuencia de números en una sola línea, separados por espacios.
'''
num1 = int(input("Introduce un número entero : "))
num2 = int(input("Introduce otro número entero: "))
if num1 < num2 :
    for i in range(num1, (num2 + 1)):
        print(i, end = " ")
else:
    for i in range(num1, num2 - 1, -1):
        print(i, end = " ")
        