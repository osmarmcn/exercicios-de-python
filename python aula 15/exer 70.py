total=0
totm=0
c=0
barato=' '
while True:
    nome=str(input('qual nome da produto: '))
    preço=float(input('preço do produto R$: '))
    c+=1
    total+=preço
    if preço > 1000:
        totm+=1
    if c ==1 or preço < menor: #pode colocar o elise com preço < menor 
        menor=preço
        barato=nome
    resp=' '
    while resp not in 'SN':
        resp= str(input('deseja continuar com as compras [S/N]')).strip().upper()[0]
    if resp =='N':
        break
print('fim da compra')
print(f'o total da compra: R$ {total} ')
print(f'produto com custo menor foi {barato}, custando: R${menor}')
print(f'o produto custa mais de 1000, sao {totm} produtos')
