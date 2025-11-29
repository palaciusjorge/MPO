import random
tiradas = []
for i in range(10):
    tiradas.append(random.randint(1, 6))
    i+=1
frecuencias = {}
for num in tiradas:
    if num in frecuencias:
        frecuencias[num] += 1
    else:
        frecuencias[num] = 1
moda = max(frecuencias, key = frecuencias.get)

print(f"La lista de resultados obtenidos en los dados es: {tiradas}.\nPor lo tanto su moda es: {moda}")


