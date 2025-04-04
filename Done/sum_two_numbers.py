test_a = False
test_b = False

while not test_a:
    print('Veuillez choisir un premier nombre')
    try:
        a = float(input('Nombre: '))
    except ValueError:
        print('Veuillez saisir un nombre valide')
    else:
        test_a = True


while not test_b:
    print('Veuillez choisir un second nombre')
    try:
        b = float(input('Nombre: '))
    except ValueError:
        print('Veuillez saisir un nombre valide')
    else:
        test_b = True
        c = float(a) + float(b)
        print(f'Le resultat de {a} + {b} est : {c}')