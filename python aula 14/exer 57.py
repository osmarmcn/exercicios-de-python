
sexo = str(input('qual seu sexo [M/F]')).strip().upper()[0] # esse zero so é para ler a primeira letra
print(sexo)
while sexo not in'MmFf':
    sexo=str(input('digite a opção correta.Tente novamente!')).strip().upper()
print('seu sexo {} foi computado'.format(sexo))