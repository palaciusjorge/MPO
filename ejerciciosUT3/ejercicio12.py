'''Escribe un programa que simule unas elecciones a delegado de clase. 
El programa debe permitir a los alumnos votar por un candidato introduciendo su nombre. 
Al finalizar la votación, el programa debe mostrar el nombre del candidato ganador y el número de votos obtenidos. Si hay un empate, el programa debe informar al usuario del primer candidato que alcanzó el número máximo de votos. 
El programa debe ejecutarse indefinidamente hasta que el usuario introduzca "FIN VOTACIONES".'''
votos = {}

print("ELECCIONES A DELEGADO DE CLASE")
print("Escribe el nombre del candidato para votar.")
print("Escribe 'FIN VOTACIONES' para terminar.\n")

while True:
    candidato = input("Voto para: ").strip().capitalize()

    if candidato.upper() == "FIN VOTACIONES":
        print("\n--- RESULTADOS ---")
        if not votos:
            print("No se registraron votos.")
            break

        max_votos = max(votos.values())

        ganador = None
        for nombre, cantidad in votos.items():
            if cantidad == max_votos:
                ganador = nombre
                break

        for nombre, cantidad in votos.items():
            print(f"{nombre}: {cantidad} voto(s)")

        print(f"\nEl ganador es {ganador} con {max_votos} voto(s).")
        break

    votos[candidato] = votos.get(candidato, 0) + 1
    print(f"Voto registrado para {candidato}. Total: {votos[candidato]}")
