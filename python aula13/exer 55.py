pmaior=0
pmenor=0
for c in range(1,6):
    peso = float(input('digite {}ª seu peso(kg): '.format(c)))
    if c ==1:
        pmaior=peso
        pmenor=peso
    else:
        if peso > pmaior:
            pmaior=peso
        if peso < pmenor:
            pmenor=peso
print('maior peso lido {} kg'.format(pmaior))
print('menor peso lido {} kg'.format(pmenor))




