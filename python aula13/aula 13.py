'''from time import sleep # estou ultizando so por diversao
for c in range(10,0,-1): # cotagem regressiva utliza o -1 para contar de 10 ate 0
    print(c)
    sleep(1)
print('fim')'''

'''from time import sleep
for c in range(1,6): #
    print('ola tudo bom') 
    sleep(1)
print('fim')'''

'''from time import sleep
for c in range(1,6):
    print(c) #no lugar de contar alguma frase escrita, vai escrever de 1 ate 6 pois 'c' é contador
    sleep(1)
print('fim')# o print fim é opcional so para dizer que acabou a contagem'''

'''from time import sleep
for c in range(1,20,2): # aqui vai ser contado de 1 ate 20 pulando duas casas ate chegar a 20 ou numero proximo no caso 19
    print(c)
    sleep(1)
print('fim')'''

'''from time import sleep
n = int(input('digite um numero: '))
for c in range(1,n): # vai ser contado ate o numero anetior do numero digitado
    print(c)
    sleep(1)'''
'''from time import sleep
n=int(input('digite um numero: '))
for c in range(0,n+1):  # n+1 para contar ate o numero que digitei / caso seja uma contagem regressiva colcoca n-1
    print(c)
    sleep(1)'''

'''i=int(input('digite um numero inicial: '))
f=int(input('digite o numero final: '))
p=int(input('numero de pulo: '))
for c in range(i,f-1,-1,): # assim ele na contagem regressiva
    print(c)'''

'''for c in range(0,3):
    n=int(input('digite um numero: ')) # a variavel vai ser escrita pela quantidade que tiver no cocntador'''
s=0
for c in range(0,5):
    n=int(input('digite um valor: '))
    s= s+n # podendo ser utilizado tambem desta forma s+=
print('a soma dos valores foi de ',s)


