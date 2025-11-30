n = int(input("Introduce la altura de la pirámide: "))

for i in range(1, n + 1):
    num_asteriscos = 2 * i - 1
    num_espacios = n - i
    fila = " " * num_espacios + "*" * num_asteriscos
    print(fila)