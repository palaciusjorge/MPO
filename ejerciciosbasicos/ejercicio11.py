'''
Escribe un programa que pida al usuario dos números enteros e imprima la secuencia de números entre ellos (incluidos) en orden ascendente. El primer número siempre será menor que el segundo.
'''
num1 = int(input("Introduce un número entero : "))
num2 = int(input("Introduce un número entero mayor que el anterior : "))
for i in range(num1, (num2 + 1)):
    print(i)