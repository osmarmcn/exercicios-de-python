


'''n = int(input('digite um numero: '))
f=1
c=n
while c > 0:
    print('{}x'.format(c), end=' ')
    f= f*c
    c-=1
print('o fatorial de {} é {}'.format(n,f))'''

'''num = 100
contador_pares = 0
while num <= 200:
    if num % 2 == 0:
        contador_pares = contador_pares + 1
    num = num + 1
print(contador_pares)'''

'''n1 = int(input('digite um numero: '))
n2 = int(input('digite outro numero: '))
c=0
while n1 <= n2:
    if n1 % 2==0:
        c+=1
    n1+=1
print('numeros pares {}'.format(c))'''

'''n1 = int(input('digite um numero: '))
n2 = int(input('digite outro numero: '))
c=0
soma=0
while n1 <= n2:
    n1 += n1
    if n1 % 2==0:
        c+=n1
        soma= soma +n1
    print(n1)
print('foram contados {} pares  e  soma delas foi de {}'.format(c,soma))'''

'''from random import randint
computador = randint(1,10)
print('qual numero escolhi? tente acertar')
print('vamos começar!!')
acertou = False
palpite = 0
soma=0
while not acertou:
    jogador = int(input('qual numero voce escolheu: '))
    palpite+=1
    soma = soma+ palpite
    if jogador==computador:
        acertou= True
    else:
        if jogador > computador:
            print('menos está perto')
        elif jogador < computador:
            print('mais você está perto')
print('você acertou com {} tentativas'.format(palpite))
print('a soma dos palpites foi {}'.format(soma))'''

'''n= int(input('digite um numero: '))
c=0
while c < n:
    c+=1
    print(c,end=' ')'''

'''from random import choice
c=0
while c <5:
    nome = str(input('digite um nome: '))
    lista = [nome]
    choice(lista)
    c+=1
print('os nomes apresentados sao em sua ordem {}'.format(lista))'''

c=0
while c == 's':
    n1 = int(input('digite um valor: '))
    n2 = int(input('digte outro valor: '))
    soma = n1+n2
    print('deseja continuar [s/n]')













