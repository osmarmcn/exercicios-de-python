soma = 0
hvelho=0
nvelho=0
mnova=0
nnova=0
for grupo in range(1,5):
    nome = str(input('digite seu nome: '))
    idade = float(input('digite sua idade: '))
    sexo = str(input('qual seu sexo: [M/F]')).upper()
    print('='*15)
    soma= idade+soma
    if grupo ==1 and sexo=='M': # pode utilizar sexo in 'Mm' colcando maiusclo ou minusculo o m
        hvelho=idade
        nvelho=nome
    if sexo =='M' and idade > hvelho:
        hvelho=idade
        nvelho=nome
    if grupo ==1 and sexo == 'F':
        mnova=idade
        nnova=nome
    if sexo == 'F' and idade < mnova:
        mnova = idade
        nnova = nome
m= soma/4
print('a media do grupo é: {}'.format(m))
print('o {} é homem mais velho com {} anos'.format(nvelho,hvelho))
print('a mulher mais nova do grupo possui {} anos e se chama {}'.format(mnova,nnova))