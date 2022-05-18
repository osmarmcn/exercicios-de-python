'''while True:
    n = int(input('digite o valor desejado: '))
    if n < 0:
        break
    for c in range(1,11):
        tabuada = n*c
        print(f'{n} x {c} = {tabuada}')
        print('vamos continuar..')
print('fim')'''
d=0
v=0
from random import randint
while True:
    computador = randint(1,10)
    jogador = int(input('mostre sua jogada: '))
    total= jogador+computador
    tipo=' '
    while tipo not in 'PI':
        tipo=str(input('qual sua jogada par ou impar [P/I]')).strip().upper()
        print(f'o jogador jogou {jogador} e o computador {computador}, obtendo o total {total}')
    if tipo =='P':
        total %2==0
        print('voce venceu!!')
        v+=1
    else:
        break
        print('voce perdeu!!')
        d+=1
    if tipo == 'I':
        total % 2==1
        print('você venceu!!')
        v+=1
    else:
        break
        print('voce perdeu')
        d+=1
print('vamos jogaaar novamente...')
print(f'total de vitorias {v}' )
print(f'total de derrotas {d}')

import
