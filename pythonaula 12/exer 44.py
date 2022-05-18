produto=float(input('valor do produto R$: '))
print('''condição de pagamento:
[1] a vista
[2] a vista no cartao
[3] parcelado em 3x sem juros
[4] parcelado em 4x ou mais com juros''')
opção = int(input('qual sua opção: '))
if opção == 1:
    v = produto - (produto*10/100)
    print('o produto a vista vale R$: {}, com desconto fica R$: {}'.format(produto,v))
elif opção == 2:
    c = produto - (produto*5/100)
    print('a vista no cartao vale R$: {}, com desconto R$: {}'.format(produto,c))
elif opção == 3:
    qp = int(input('qauntas parcelas: ')) #qp = quantidade de parcelas
    par = produto/qp
    print('seu produto vai ser parceldo em {}x, ficando R$; {}'.format(qp,par))
elif opção == 4:
    v = produto + (produto*20/100)
    qp = int(input('quantas parcelas vai querer: '))
    tparc = v/qp # tparc = total de parcelas
    print('o valor do produto parcelado em 4x ou mais fica R$: {}'.format(v))
    print('o valor de cada parcela vai ficar R$:{:.2f}'.format(tparc))
else:
    print('opção invalida. Tente novamente!')

