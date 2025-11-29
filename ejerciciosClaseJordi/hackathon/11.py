import random
import string
def generar_password(longitud):
    if longitud < 4:
        raise ValueError("La longitud de la contraseña no puede ser menor que 4.")
    minusculas = string.ascii_lowercase
    mayusculas = string.ascii_uppercase
    numeros = string.digits
    especiales = "!@#$%&*?_-"
    password = [
        random.choice(minusculas),
        random.choice(mayusculas),
        random.choice(numeros),
        random.choice(especiales)
    ]
    todos = minusculas + mayusculas + numeros + especiales
    for _ in range(longitud):
        password.append(random.choice(todos))
    random.shuffle(password)
    return "".join(password)
longitud = int(input(f"Introduce la longitud que quieres para tu contraseña: "))
print(f"Tu contraseña es la siguiente: {generar_password(longitud)}")

        
