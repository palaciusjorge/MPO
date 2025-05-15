import random
num = random.randint(1,100)
intento = int(input("¿Qué número crees que es entre 1 y 100?"))
contador = 0
while num != intento:
    if intento > num:
        print("Vaya, te has pasado, el número es más pequeño")
    else:
        print("Te has quedado corto, el número es más grande")
    intento = int(input("Prueba de nuevo :"))
    contador += 1
print(f"Has acertado, solo te ha costado {contador} intentos adivinar el número")


