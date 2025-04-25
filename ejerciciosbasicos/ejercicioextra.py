dimension = int(input("Introduce la dimensión del cuadrado (tiene que ser un numero impar para que salga bien): "))

for i in range(dimension):
    for j in range(dimension):
        if i == j or i + j == dimension - 1 or i == 0 or i == dimension - 1 or j == 0 or j == dimension - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()