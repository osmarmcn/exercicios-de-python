n=0
s=0
c=0
n = int(input('digite um valor: '))
while n != 999:
    s= s+n
    c+=1
    n = int(input('digite um valor: '))
print('fim')
print('a soma dos numeros digitados foi de {}'.format(s))
print('foram digitados {} numeros'.format(c))

#para retirar o valor de 999 pode ser feito s - 999 a contagem tbm com c-1
#pode ainda ser feito repetir o comando de ler e colocado fora da variavel assim nao sera lido o 999
# tendo que colocar o comando no final assim não efetivando a soma
#pois os comandos de soma e contagem estao acima assim nao podendo fazer a soma do 999

'''s=0
n=0
c=0
while n != 999:
    n= int(input('digite um valor: '))
    s= s+n
    c+=1
print('a soma dos valores foi de: {} e a contagem de {}'.format(s-999,c-1))'''
