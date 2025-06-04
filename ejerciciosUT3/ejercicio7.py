'''
Escribe un programa que almacene en un diccionario las capitales de varios países, 
se introducirán los datos con la forma PAIS-CAPITAL. Esto debe ejecutarse 
indefinidamente hasta que el usuario introduzca "FIN INSERCIONES". 
El programa debe permitir al usuario consultar la capital de un país introduciendo 
su nombre. Si el país no está en el diccionario, el programa debe informar al usuario.
'''
paises = {}
entrada = input("Introduce un país y su capital con el formato: PAIS - CAPITAL, o escribe FIN INSERCIONES para finalizar\n").lower()
while entrada != "fin inserciones":
    pais = entrada.split("-")[0]
    capital = entrada.split("-")[1]
    paises[pais] = capital
    entrada = input("Introduce un país y su capital con el formato: PAIS - CAPITAL, o escribe FIN INSERCIONES para finalizar\n").lower()
pais_usuario = input("Introduce el pais que quieres consultar: ").lower()
if pais_usuario in paises:
    print(f"La capital de {pais_usuario.capitalize()} es {paises[pais_usuario].capitalize()}.")
else:
    print(f"El pais {pais_usuario.capitalize()} no esta introducido en nuestro diccionario")


