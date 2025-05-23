entero = int(input("Introduce un numero entero: "))
factorial = 1
for i in range (entero):
    if entero != 0:
        factorial = factorial * (i + 1)
    else:
        break
    
    
print (factorial)