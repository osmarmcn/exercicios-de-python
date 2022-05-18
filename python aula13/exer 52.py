'''total =0
n=int(input('digite um numero:'))
for c in range(1, n+1):
    if n % c ==0:
        print('\033[34m',end='')
        total+=1
    else:
        print('\033[32m',end= '')
    print(c)
print('\033[0mo numero {} foi dividido {} vezes'.format(n,total))
if total == 2:
    print('\033[0mo numero {} é primo'.format(n))
else:
    print('\033[0mo numero {} nao é primo'.format(n))'''


num = int(input('digite um numero: '))
tot=0
for c in range(1,num+1):
    if num % c ==0:
        print('\033[33m', end='') # a utlização de cores so para indicar quantos sao divisiveis
        tot+=1 # o tot é para saber quantas vezes o numero pode ser dividido
    else:
        print('\033[32m', end='')
    print('{}'.format(c), end=' ')
print('\nO numero {} é divisivel até {}'.format(num,tot))
if tot <=2: # tm que ficar fora do laço para saber se é divisvel ate 2 numeros
    print('numero é primo')
else:
    print('o numero nao é primo')


