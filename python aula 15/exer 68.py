from random import randint
v=0
while True:
    jogador= int(input('digite um valor: '))
    computador = randint(1, 10)
    total = jogador+computador
    tipo = ' '
    while tipo not in 'PI':
        tipo=str(input('qual tipo que você escolhe par ou impar [P/I]')).strip().upper()
    print(f'o jogador jogou {jogador} e computador {computador} obtendo o e resultado{total}')
    if tipo == 'P':
        if total % 2 ==0:
            v+=1
            print('você venceu!')
        else:
            print('você perdeu!!')
            break
    elif tipo == 'I':
        if total %2==1:
            v+=1
            print('você venceu!!')
        else:
            print('voce perdeu!!')
            break
    print('vamos jogar novamente...')
print(f'você venceu {v} partidas')










