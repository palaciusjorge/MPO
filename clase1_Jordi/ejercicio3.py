#EJERCICIO 3

num = int(input("Introduce un numero entero : "))
if num % 3 == 0:
    if num % 5 == 0:
        print(f"El numero {num} es divisible por 3 y 5")
    else:
        print(f"El numero {num} es divisible por 3 pero no por 5")
elif num % 5 == 0:
    print(f"El numero {num} es divisible por 5 pero no por 3")
else:
    print(f"El numero {num} no es divisible por 3 ni por 5")
    