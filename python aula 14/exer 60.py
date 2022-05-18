'''from math import factorial
n=int(input('digite um numero: '))
f= factorial(n)
print('o fatorial de {} é {}'.format(n,f))'''

'''n=int(input('digite um numero: '))
c= n
f=1
while c > 0:
    print('{}x'.format(c), end=' ')
    f=f*c
    c-=1
print('o fatorial de {} é: {}'.format(n,f))'''

n = int(input('digite um valor: '))
c = 1
f= 1
for c in range(1,n+1):
    print('{}x'.format(c),end=' ')
    f= f*c
    c-=1
print('o valor do fatorial de {} é: {}'.format(n,f))

