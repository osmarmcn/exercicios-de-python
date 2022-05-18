total=0
totm=0
totf=0
while True:
    nome=str(input('digite seu nome: '))
    idade=int(input('digite sua idade: '))
    sexo=' '
    while sexo not in 'MF':
        sexo=str(input('digite seu sexo: ')).strip().upper()[0]
        if idade >=18:
            total+=1
        if sexo == 'M':
            totm+=1
        if sexo == 'F' and idade < 20:
            totf+=1
    resp=' '
    while resp not in 'SN':
        resp= str(input('deseja continuar [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'o total de pessoas com mais de 18 anos é {total}')
print(f'foram cadastrado {totm} homens')
print(f'foram cadastrada {totf} mulheres com menos de 20 anos')


