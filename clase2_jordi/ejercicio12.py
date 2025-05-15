entero = int(input("Introduce un numero entero : "))
maximo = 0
minimo = entero
while entero != 0:
    if entero > maximo:
        maximo = entero
    elif entero < minimo:
        minimo = entero
    entero = int(input("Introduce otro numero entero (para salir del bucle introduce 0) : "))
print(f"El maximo es {maximo} y el minimo es {minimo}")

