velocidade = int(input('a velocidade de momento é:'))
print('o carro esta a {} km/h'.format(velocidade))
if velocidade >80: # deve ser o sinal de maior que 80
    print('você ultrapassou o limite de velocidade estabecido, sendo assim, multado!')
    m = (velocidade-80)*7 #deve pegar velocidade excedente e diminuir por 80
    print('o motorista foi multado em R$ {}'.format(m))
else:
    print('esta dentro do permito, boa viagem!!')

'''v1 =float(input('velocidade de momento é:')) # programa com defeito nao cabe utilização
v2 =float(input('a velocidade de momento é:'))
v3 =float(input('a velocidade de momento é:'))
print('os carros estao respectivamente a {} km/h, {} km/h e {} km/h'.format(v1,v2, v3))
if v1 > 80 and v2 > 80 and v3 > 80:
    print('você {} foi multado excedeu a quilometragem permitida'.format(v1))
    print('você {} foi multado excedeu a quilometragem permitida'.format(v2))
    print('você {} foi multado excedeu a quilometragem permitida'.format(v3))
else:
    print('está dentro do permitido, boa viagem!!!')'''
