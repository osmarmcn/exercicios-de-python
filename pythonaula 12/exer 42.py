

l1 = int(input('lado 1:'))
l2 = int(input('lado 2: '))
l3 = int(input('lado 3: '))
if l1 < l2+l3 and l2 < l3+l1 and l3 < l2+l1:
    print('podem forma um triangulo', and =' ')
    if l1 ==l2 and l2 ==l3 and l3 == l1: #podendo ser feito de outra forma: l1==l2==l3
        print('triangulo equilatero') # se quiser a frase 'triangulo equilatero' no primeiro print so colocar end=' '
    elif l1 != l2 != l3: #podendo ser feito de outra forma: l1 != l2 !=l3
        print('triangulo escaleno') # != esse simbolo é sinal de diferente
    else:
        print('triangulo isoceles')
else:
    print('nao forma um triangulo')