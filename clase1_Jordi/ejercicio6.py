#EJERCICIO 6

year = int(input("Dime que año quieres saber si es bisiesto : "))
if ((year%4==0 and year%100!=0) or (year%400 == 0)):
    print(f"El año {year} es bisiesto")
else:
    print(f"El  a;o {year} no es bisiesto")
    