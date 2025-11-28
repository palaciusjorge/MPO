x = int(input("Introduce el precio del producto: ")) 
y = int(input("Introduce el descuento a aplicar: "))
print(f"El precio final es: {x - (x*y/100):.2f} $")


