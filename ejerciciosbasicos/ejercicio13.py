'''
Escribe un programa que pida al usuario un número entero positivo e imprima la tabla de multiplicar de ese número (del 1 al 10).
'''
entero = int(input("Introduce un número del 1 al 10: "))
for i in range (10):
    print(f"{entero} * {i + 1} = {entero * (i + 1)}")
