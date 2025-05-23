'''
Escribe un programa que pida al usuario cuantas evaluaciones hay que cualificar. 
Seguidamente se recibirán ese número de series de notas (números decimales entre 0 y 10) y calcule la media de esas notas.
El programa debe seguir pidiendo notas hasta que el usuario ingrese un -1. Al final, imprime la media.
'''
numero_evaluaciones = int(input("Introduzca el número de evaluaciones :"))
for i in range(numero_evaluaciones):
    nota = float(input(f"Introduzca la siguiente nota de la {i + 1} evaluación (para terminar escriba -1) : "))
    suma_notas = 0
    num_notas = 0
    while nota != -1:
        suma_notas += nota
        num_notas += 1
        nota = float(input(f"Introduzca la siguiente nota de la {i + 1} evaluación (para terminar escriba -1) : "))
    print(f"La nota media de la evaluación {i + 1} es : {(suma_notas/num_notas)}")
        

