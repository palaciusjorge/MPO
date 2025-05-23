
esCero = False
sumatorio = 0
'''
La solución de clase es mejor porque no obliga a entrar en el bucle.
'''
while esCero == False :
    num = int(input("Introduce un numero entero :"))
    if num == 0:
        esCero = True
    else:
        sumatorio += num
print (sumatorio)
