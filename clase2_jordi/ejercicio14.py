
from sympy import isprime

def es_primo(n):
    return isprime(n)

entero = int(input("Introduzca el número que quiere saber si es primo o no : "))
if es_primo(entero):
    print(f"El numero {entero} es primo")
else:
    print(f"El numero {entero} no es primo")
