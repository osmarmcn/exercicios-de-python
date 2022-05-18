from random import randint
from time import sleep
itens = ('pedra','papel','tesoura')
comp = randint(0,2)
print('''qual sua opçâo:
[1] pedra
[2] papel
[3] tesoura''')
print('-='*15)
jogador = int(input('qual sua opção: '))
print('-='*15)
print('jo')
sleep(1)
print('ken')
sleep(1)
print('pô!!!')
print('o computador escolheu {}'.format(itens[comp])) # itens colcodo ai serve para o cumputador ler a lista, pois ele so ler os numeros de 0a 2 da lsita designada
print('o jogador escolheu {}'.format(itens[jogador]))
if comp == 0:
    if jogador == 0:
        print('jogo empatado')
    elif jogador == 1:
        print('jogador venceu!')
    elif jogador == 2:
        print('comp venceu!')
elif comp == 1:
    if jogador == 0:
        print('jogador venceu!')
    elif jogador == 1:
        print('jogo empatado')
    elif jogador == 2:
        print('jogador venceu!')
elif comp == 2:
    if jogador == 0:
        print('jogador venceu!')
    elif jogador == 1:
        print('comp venceu!')
    elif jogador == 2:
        print('jogo empatado')









































