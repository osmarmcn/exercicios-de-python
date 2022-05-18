'''priemiro = int(input('digite um numero: '))
razão = int(input('digite um numero: '))
termo = priemiro
c=1
total=0
mais=10
while mais !=0:
    total = total+mais
    while c<=total:
        print('{} - '.format(termo),end=' ')
        termo+=razão
        c+=1
    print('pausa')
    mais = int(input('deseja escolher mais algum termo?: '))
print('fim')
print('foram apresentados {} termos'.format(total))'''














primeiro = int(input('digite um valor: '))
razão = int(input('digite a razão: '))
termo = primeiro
c = 0
acrescimo=10
total=0
while acrescimo !=0:
    total= total+acrescimo
    while c<=total:
        print('{} - '.format(termo),end=' ')
        termo = termo + razão
        c+=1
    print('pausa')
    acrescimo = int(input('deseja acresntar mais algum termo? '))
print('fim')
print('foram utlizados {} termos'.format(total))