'''for c in range (0,31,3):
    print(c)
print('fim')'''

'''c=1
while c<10:
    print(c, end=' ')
    c+=1'''

'''n=1
while n != 0:
    n=int(input('digite um numero: '))
print('fim')'''


'''r= 'S'
while r == 'S':
    n=int(input('digite um valor: '))
    r=str(input('deseja continuar [S/N]')).upper()'''

n=1
par=impar=0
while n != 0:
    n=int(input('digite um valor: '))
    if n !=0:
        if n % 2== 0:
            par +=1
        else:
            impar+=1
print('foram digitados {} pares e {} imapres'.format(par,impar))



