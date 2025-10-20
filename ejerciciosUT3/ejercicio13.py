paises = {}
entrada = input("Introduce un país y su capital con el formato: PAIS - CAPITAL, o escribe FIN INSERCIONES para finalizar\n").lower()

while entrada != "fin inserciones":
    partes = entrada.split("-")
    if len(partes) == 2:
        pais = partes[0].strip()
        capital = partes[1].strip()
        paises[pais] = capital
    else:
        print("Formato incorrecto. Usa el formato: PAIS - CAPITAL.")
    entrada = input("Introduce un país y su capital con el formato: PAIS - CAPITAL, o escribe FIN INSERCIONES para finalizar\n").lower()

consulta = input("¿Quieres buscar por 'pais' o por 'capital'? ").strip().lower()

if consulta == "pais":
    pais_usuario = input("Introduce el país que quieres consultar: ").lower()
    if pais_usuario in paises:
        print(f"La capital de {pais_usuario.capitalize()} es {paises[pais_usuario].capitalize()}.")
    else:
        print(f"El país {pais_usuario.capitalize()} no está introducido.")
elif consulta == "capital":
    capital_usuario = input("Introduce la capital que quieres consultar: ").lower()
    pais_encontrado = next((pais for pais, capital in paises.items() if capital == capital_usuario), None)
    if pais_encontrado:
        print(f"{capital_usuario.capitalize()} es la capital de {pais_encontrado.capitalize()}.")
    else:
        print(f"No se encontró ningún país con la capital {capital_usuario.capitalize()}.")
else:
    print("Opción no válida.")