from datetime import date
atual = date.today().year
atleta = str(input('qual nome do alteta: '))
nasc = int(input('que ano nasceu: '))
idade = atual - nasc
if 4 > idade <= 9:
    print('categoria mirim')
elif 9 > idade < 14:
    print('categoria juvenil ')
elif idade > 14 and idade < 18:
    print('categoria infatojuvenil')
elif idade > 18:
    print('categoria adulto')
elif idade > 30:
    print('categoria master')
