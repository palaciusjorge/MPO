num_int = int(input("Introduce un numero entero positivo : "))
while num_int != -1:
    digitos = 0
    if num_int == 0:
        digitos = 1
    else:
        temp = num_int
        while temp > 0:
            temp = temp//10
            digitos += 1
    print(f"El numero {num_int} tiene {digitos} cifras")
    num_int = int(input("Introduce otro entero positivo (escribe -1 para salir del bucle) : "))
