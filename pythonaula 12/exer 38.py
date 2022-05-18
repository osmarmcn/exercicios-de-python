n1 = int(input('digite um numero: '))
n2 = int(input('digite outro numero: '))
if n1 > n2:
    print('o primeiro numero {} é maior'.format(n1))
elif n2 > n1:
    print('o segundo numero {} é maior'.format(n2))
else:
    print('os numeros de {} e {} iguais'.format(n1,n2))