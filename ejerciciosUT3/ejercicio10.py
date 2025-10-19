'''Escribe un programa que pida al usuario una lista de números enteros separados por comas y almacene estos números en una tupla. 
Luego, el programa debe calcular y mostrar la suma, el promedio, el número máximo y el número mínimo de la tupla.'''
entrada = input("Introduce una lista de números enteros separados por comas: ")

numeros = tuple(int(num.strip()) for num in entrada.split(","))

suma = sum(numeros)
promedio = suma / len(numeros)
maximo = max(numeros)
minimo = min(numeros)

print("\n--- RESULTADOS ---")
print(f"Tupla: {numeros}")
print(f"Suma: {suma}")
print(f"Promedio: {promedio:.2f}")
print(f"Máximo: {maximo}")
print(f"Mínimo: {minimo}")