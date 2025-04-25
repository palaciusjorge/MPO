#bucle que nos diga cuantos numeros pares hay entre 0 y el numero que nos pida el usuario
entero = int(input("Introduce un numero entero :"))
lista = []
contador = 0
for i in range (entero +1):
    if i % 2 == 0:
        lista.append(i)
        contador += 1
    else:
        continue
print(f"Hay un total de {contador} números pares, y son los siguientes : {lista}")

