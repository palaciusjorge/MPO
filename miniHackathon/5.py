'''
Lista de dos niveles
'''
from tabulate import tabulate
lista_notas = [["Jorge", 7, 6, 6, 10], ["Irene", 10, 9 , 10, 8], ["Gabriel", 5, 5, 10, 8]]
encabezados = ['Nombre', 'Nota 1', "Nota 2", "Nota 3", "Nota 4"]
print(tabulate(lista_notas, headers=encabezados, tablefmt="grid"))
for elemento in lista_notas:
    nombre = elemento[0]
    notas = elemento[1:]
    media = sum(notas)/len(notas)
    print(f"El alumno {nombre} tiene una media de: {media}")

'''
Tabla que encontre en foros sin usar IA: 
print(f"{encabezados[0]:<10} {encabezados[1]:<5} {encabezados[2]:<10}")

print("-" * 30)

for fila in lista_notas:
    print(f"{fila[0]:<10} {fila[1]:<5} {fila[2]:<10}")
'''
        

