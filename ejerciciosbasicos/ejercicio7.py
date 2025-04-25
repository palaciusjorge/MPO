#EJERCICIO 7

num1 = float(input("Introduce un numero : "))
num2 = float(input("Introduce otro numero : "))
operador = str(input("Introduce la operacion que deseas hacer : sumar, restar, multiplicar, dividir : "))
if operador in ['sumar', 'restar','multiplicar', 'dividir']:
    if operador == 'sumar':
        print(f"La suma es : {num1 + num2}")
    elif operador == 'restar':
        print(f"La resta es : {num1 - num2}")
    elif operador == 'multiplicar':
        print(f'La multiplicaión es  : {num1 * num2}')
    else:
        print(f'La división es : {num1 / num2}')
else:
    print("El operador introducido no es valido, por favor escribelo igual que en las opciones que te da el programa")