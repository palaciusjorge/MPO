import random
import time
deadpool_health = int(input("¿Cuanta vida tendrá Deadpool? "))
wolverine_health = int(input("¿Cuanta vida tendrá Wolverine? "))
turn = 0
regenerate = False

while deadpool_health > 0 and wolverine_health >0:

    turn += 1
    print(f"\nEste es el turno {turn}")

    #Deadpool ataca a Wolverine
    if regenerate:
        print("Deadpool ha recibido un golpe critico y tiene que regenerarse")
        regenerate = False

    elif  random.random() > 0.2 :
        deadpool_damage = random.randint(10,100)
        if deadpool_damage == 100:
            print("Deadpool asesta un golpe crítico! Wolverine no ataca en el siguiente turno")
            regenerate = True
        else:
            print(f"Deadpool ha hecho {deadpool_damage} de daño con su ataque.")


        wolverine_health -= deadpool_damage
        if wolverine_health <= 0:
            print("Wolverine ha perdido toda su vida")
            break
        else:
            print(f"Vida restande de wolverine: {wolverine_health}")
    else:
        print("Wolverine ha esquivado el ataque!")


    #Wolverine ataca a Deadpool
    if regenerate:
        print("Wolverine ha recibido un golpe crítico y tiene que regenerarse")
        regenerate = False

    elif random.random() > 0.25 :
        wolverine_damage = random.randint(10,120)
        if wolverine_damage == 120:
            print("Wolverine crítico! Deadpool no ataca en el siguiente turno")
            regenerate = True
        else:
            print(f"Wolverine ha hecho {wolverine_damage} de daño con su ataque.")
            

        deadpool_health -= wolverine_damage
            
        if deadpool_health <= 0:
            print("Deadpool ha perdido toda su vida.")
            break
        else:
            print(f"Vida restante de Deadpool: {deadpool_health}")
            
        if deadpool_health <= 0:
            break
    else:
        print("Deadpool ha esquivado el ataque")
    time.sleep(2)
if deadpool_health > 0:
    print("Deadpool ha ganado la pelea.")
else:
    print("Wolverine ha ganado la pelea.")
    


