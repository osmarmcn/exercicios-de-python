n1 = int(input('digite um nuemro: '))
n2 = int(input('digite outro numero: '))
opção=0
while opção !=5:
    print('''escolha o que deseja fazer:'
    [1]soma
    [2]mutiplicar
    [3]maior
    [4]novos numeros
    [5]sair''')
    opção= int(input('qual sua opção: '))
    if opção==1:
        soma = n1+n2
        print('a soma de {} e {} é: {}'.format(n1,n2,soma))
    elif opção==2:
        mult = n1*n2
        print('a multiplicação de {} e {} da o resultado: {}'.format(n1,n2,mult))
    elif opção==3:
        if n1 > n2:
            maior=n1
            print('o valor de n1 é maior')
        else:
            maior=n2
            print('o valor de n2 é maior')
    elif opção==4:
        print('informe os numeros novamente')
        n1=int(input('digite um numero: '))
        n2=int(input('digite outro numero: '))
    elif opção==5:
        print('terminando!')
    else:
        print('opção invalida')
print('fim do programa!')