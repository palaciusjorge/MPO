#EJERCICIO 4

num = float(input("Introduce la nota del alumno : "))
if num < 0:
    print("Nota no valida, no puede tener nota negativa")
elif 0<= num < 4.5:
    print("El alumno esta suspenso")
elif 4.5<= num < 5:
    print("El alumno esta en el limbo del aprobado, depende de su comportamiento")
elif 5 <= num < 7:
    print("El alumno tiene un Suficiente")
elif 7<=9:
    print("El alumno tiene un notable")
else:
    print("El alumno tiene un sobresaliente")
    
