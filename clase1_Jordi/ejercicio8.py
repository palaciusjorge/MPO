#EJERCICIO 8

mes = str(input('Qué mes quieres saber cuantos dias tiene : ')).lower()
if mes in ['enero', 'marzo', 'mayo', 'julio', 'agosto', 'octubre', 'diciembre']:
    print(f'{mes} tiene 31 días')
elif mes in ['abril', 'junio', 'septiembre', 'noviembre']:
    print(f'{mes} tiene 30 días')
elif mes == 'febrero':
    year = int(input("Dime que año es : "))
    if ((year%4==0 and year%100!=0) or (year%400 == 0)):
        print(f'Este año {mes} tiene 29 días')
    else:
        print(f'Este año {mes} tiene 28 días')
else:
    print('No has intruducido un mes válido')
    