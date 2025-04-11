#EJERCICIO 10

dia = int(input("¿Que día es hoy? "))
mes = str(input("¿De qué mes? ")).lower()
year = int(input("¿De qué año? "))
if mes in ['enero', 'marzo', 'mayo', 'julio', 'agosto', 'octubre', 'diciembre']:
    if 0 < dia <= 31:
        print("Has introducido un día válido")
    elif dia > 31:
        print("Ese mes no tiene tantos días")
    else:
        print("¿Cómo va a ser un día negativo?")
elif mes in ['abril', 'junio', 'septiembre', 'noviembre']:
    if 0 < dia <= 30:
        print("Has introducido un día válido")
    elif dia > 30:
        print("Ese mes no tiene tantos días")
    else:
        print("¿Cómo va a ser un día negativo?")
elif mes == 'febrero':
    if ((year%4==0 and year%100!=0) or (year%400 == 0)):
        if 0 < dia <= 29:
            print("Has introducido un día válido")
        elif dia > 29:
            print("Ese mes no tiene tantos días")
        else:
            print("¿Cómo va a ser un día negativo?")
    else:
        if 0 < dia <= 28:
            print("Has introducido un día válido")
        elif dia > 28:
            print("Ese mes no tiene tantos días")
        else:
            print("¿Cómo va a ser un día negativo?")
else:
    print("Ese mes no es válido")



    