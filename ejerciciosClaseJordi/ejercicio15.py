'''
Escribe un programa que simule una cuenta bancaria. El programa debe permitir al usuario realizar las siguientes operaciones:

1. Ingresar dinero
2. Retirar dinero
3. Consultar saldo
4. Salir

Inicializa el saldo en 0 y permite al usuario realizar operaciones hasta que decida salir.
'''

saldo = 0
print("Bienvenido a tu cuenta bancaria ")
while True:
    print()
    print("1. Ingresar dinero")
    print("2. Retirar dinero")
    print("3. Consultar saldo")
    print("4. Salir")

    option = input("¿Qué quieres hacer? ")
    match option:
        case "1":
            saldo += int(input("¿Cuánto dinero quiere ingresar? "))
            print(f"Tu saldo actual se ha actualizado, ahora mismo tienes {saldo}$ en la cuenta.")
        case "2":
            saldo -= int(input("¿Cuánto dinero quieres retirar? "))
            print(f"Tu saldo se ha actualizado, acutalmiente tienes {saldo}$ en la cuenta.")
        case "3":
            print(f"Tu saldo actual es {saldo}$.")
        case "4":
            print("Gracias por usar nuestros servicios, hasta la próxima!")
            break

