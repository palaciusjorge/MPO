#EJERCICIO 1: Escribe un programa que pida al usuario un número entero y determine si es par o impar. El programa debe imprimir un mensaje indicando el resultado.
num = int(input("Introduzca un numero entero :"))
if num % 2 == 0 :
    print(f"El numero {num} es par")
else:
    print(f"El numero {num} es impar")