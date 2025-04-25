#EJERCICIO 9

precio = float(input("¿Cuánto cuesta el artículo que quieres? "))
if 95 < precio < 100:
    print("Te queda muy poco para llegar a los 100 euros y conseguir un descuento del 10%, ¿quieres mirar otro producto?")
elif 100 <= precio:
    print(f'Enhorabuena, has conseguido un 10% de descuento, la cantidad a pagar finalmente es : {precio - precio*0.1}')
else:
    print(f'El total de la cuenta es {precio}')
    