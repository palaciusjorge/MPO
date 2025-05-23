'''
Escribe un programa que reciba números hasta la introducción de un 0. 
Por cada número, suponiendo que el 1 representa el lunes, el 2 el martes, etc., imprime el nombre del día correspondiente.
'''
semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes","Sábado", "Domingo"]
num = int(input("Introduce un numero entero : "))
while num != 0:
    print(f"El dia de la semana correspondiente a ese numero es : {semana[(num%7) - 1]}")
    num = int(input("Introduce otro dia, (recuerda escribir 0 si quieres salir) : "))
print("Has salido del bucle")