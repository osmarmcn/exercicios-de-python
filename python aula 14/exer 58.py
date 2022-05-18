from random import randint
comp = randint(0,10)
print('pensei nesse numero qual numero escolhi entre 0 e 10')
acertou = False
palpite=0
while not acertou:
    jogador = int(input('qual seu palpite ?:'))
    palpite+=1
    if jogador == comp:
        acertou = True
    else:
        if jogador < comp:
            print('mais... esta perto')
        elif jogador > comp:
            print('menos... esta perto')
print('você acertou com {} tentativas'.format(palpite))

