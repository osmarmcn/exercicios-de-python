'''ano = int(input('qual ano desejo saber?:'))
bissexto = ano % 4
if ano % 4 ==0 and ano % 100 !=0 or ano % 400==0:
    print(' o ano {} é bissexto'.format(ano))
else:
    print('o ano {} nao é bissexto'.format(ano)'''

import calendar # procurar como usar correntamente 
ano = str(input('digite o ano:'))
if calendar.isleap(ano):
    print('ano bissexto')
else:
    print('não é bissexto')