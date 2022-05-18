soma=0
cont=0
for c in range(1,7):
    n=int(input('digite um  numero: '))
    if n % 2 ==0:
        soma= soma+n
        cont += 1
print('a soma dos numeros pares digitado: {}'.format(soma))
print('foram contados {} numeros pares'.format(cont))
