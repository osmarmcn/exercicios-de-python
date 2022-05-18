'''from random import randint
comp = randint(0,5)
eu = int(input('qual numero eu pensei?:'))
if eu == comp:
    print('Parabéns, você me ganhou!')
else:
    print('ganhei! pensei no numero {} e nao no {}'.format(comp, eu)'''
import playsound

'''from random import choice
print('vou pensar em um numero entre 0 e 5, tente advinhar')
lista = [0,1,2,3,4,5]
escolha = choice(lista)
eu = int(input('qual numero pensei?:'))
if eu==escolha:
    print('Parabéns! você acertou.')
else:
    print('pensei no numero {} e não no {}'.format(escolha, eu))'''

'''from random import choice
print('vou pensar em um nome para completar o meu:')
lista = ['joao', 'amaral','jose', 'lucas', 'filho', 'amadeu']
escolha = choice(lista)
n1 = str(input('qual nome eu pensei foi:'))
if n1==escolha:
    print('Parabéns! Você acertou o nome que eu desejava Pedro!!!!')
else:
    print('foi escolhido o nome Pedro {}, contudo, foi outro nome escolhido, o Pedro {}'.format(escolha, n1))'''

'''from random import randint
from playsound import playsound
escolha = randint(0,1)
print('vou escolher um numero')
n1 = int(input('o numero que pensei foi:'))
if n1==escolha:
    print('Você acertou, Parabéns!!!')
    playsound.playsound('ex21.mp3') #esta apresentando erro  preciso ver posteriomente para corrigir!
else:
    print('que pena voce erroooouuuu!!!!')'''

import pygame
import random
sorteio = random.randint(0,1)
print('vou escolher um numero')
pessoa = int(input('o numero que imaginei foi:'))
if pessoa == sorteio:
    print('Você acertou, muit bem!!')
    pygame.init() # a musica nao tocou, mas a leitura do programa deu certo
    pygame.mixer.music.load('ex21.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()
else:
    print('infelizmente você errou. {} sendo que era {}'.format(sorteio, pessoa))



