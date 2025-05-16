def decimal_a_binario(numero):
    if numero == 0:
        return "0"
    
    binario = ""
    while numero > 0:
        residuo = numero % 2
        binario += str(residuo)
        numero = numero // 2
    return binario[::-1]

numero = int(input("Ingrese un número entero positivo: "))
if numero < 0:
    print("Por favor ingrese un número positivo.")
else:
    resultado = decimal_a_binario(numero)
    print(f"El número {numero} en binario es: {resultado}")