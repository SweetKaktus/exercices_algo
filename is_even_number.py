test = False

a = 0

while not test:
    print('Veuillez indiquer un nombre')
    try:
        a = float(input('Nombre: '))
    except ValueError:
        print('Veuillez saisir un nombre valide')
    else:
        test = True

if a % 2 == 0:
    print(f'{a} est un nombre pair')
else:
    print(f'{a} est un nombre impair')