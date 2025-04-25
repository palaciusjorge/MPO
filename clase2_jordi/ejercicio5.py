entero = int(input("Introduce un numero entero: "))
for i in range (entero + 1):
    if (i % 3 == 0) and (i % 5 == 0):
        continue
    if i % 3 == 0:
        print(f"{i} es múltiplo de 3 y está en el rango del entero introducido")
    if i % 5 == 0:
            print(f"{i} es múltiplo de 5 y está en el rango del entero introducido")
    else:
        continue
    
    