edad = int(input("Introduce tu edad: "))
if edad < 0 :
    print("Edad no valida")
elif edad<=12:
    print("Eres un niño/a")
elif edad <= 17:
    print("Eres un adolescente")
elif edad <= 64:
    print("Eres un adulto/a")
else:
    print("Eres senior")
