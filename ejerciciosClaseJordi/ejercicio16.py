'''
Escribe un programa que pida al usuario un número entero positivo y determine si es un número perfecto o no. 
Un número perfecto es aquel que es igual a la suma de sus divisores propios (excluyendo el propio número). Por ejemplo, 6 es un número perfecto porque sus divisores son 1, 2 y 3, y 1 + 2 + 3 = 6.
'''

def is_perfect(n):
    if n <= 0:
        return False
    
    suma_divisores = 0
    for i in range(1, n//2 + 1):
        if n % i == 0:
            suma_divisores += i
    
    return suma_divisores == n

numero = int(input("Ingrese un número entero positivo: "))
if is_perfect(numero):
    print(f"{numero} es un número perfecto.")
else:
    print(f"{numero} no es un número perfecto.")