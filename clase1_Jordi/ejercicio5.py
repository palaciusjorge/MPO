#EJERCICIO 5

dia = str(input("Introduce un dia de la semana : ")).lower()
if dia in ['lunes', 'martes', 'miércoles', 'jueves', 'viernes']:
    print("Hot te toca currar, que aún no es finde")
elif dia == 'miercoles':
    print('Te digo que estamos entre semana, pero toca repasar ortografía')
elif dia in ['sábado', 'domingo']:
    print("Es fin de semana, ¡a disfrutar!")
elif dia == 'sabado':
    print("Estamos en fin de semana, pero repasa las tildes")
else:
    print("No has introducido un dia de la semana")