'''from datetime import date
atual = date.today().year
totalme = 0
totalma =0
for pessoa in range(1,7):
    nasc = int(input('nasceu em  que ano: '))
    idade = atual - nasc
    if idade >18:
         totalma+=1
    else:
        totalme+=1
print('ao todo {} atigiram a maioridade e {} ainda nao atingiram'.format(totalma,totalme))'''

from datetime import date
atual = date.today().year
tmaior=0
tmenor=0
for c in range(1,8):
    nasc = int(input('digite o seu ano de nascimento {}ª : '.format(c)))
    idade = atual - nasc
    print('essa pessoa tem {} ano'.format(idade))
    if idade > 18:
        tmaior+=1
    else:
        tmenor+=1
print('sao {} maiores de 18 anos'.format(tmaior))
print('sao {} menores de 18 anos'.format(tmenor))












