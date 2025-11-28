cadena_texto = input("Introduce un texto: ")
contador_mayus = 0
contador_minus = 0
for p in cadena_texto:
        if p.isupper():
            contador_mayus += 1
        elif p.islower():
            contador_minus += 1
print(f"En el texto hay: {contador_mayus} letras mayusculas, {contador_minus} letras minusculas.")


