primeiro = int(input('digite um numero: '))
razão = int(input('digite a razão: '))
termo = primeiro
c=1
while c <=10:
    print('{}->'.format(termo),end=' ')
    termo = termo +razão
    c+=1
print('fim')