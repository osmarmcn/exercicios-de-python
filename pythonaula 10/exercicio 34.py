salario = float(input('qual seu salario?:'))
if salario >1250:
    aumento = salario + (salario*10/100)
    print('o salario atual do funcionario é R$ {}, com reajuste {}'.format(salario,aumento))
else:
    reajsute = salario + (salario*15/100)
    print('o saalrio atual é de R$ {}, sendo reajsutado R$ {}'.format(salario,reajsute))
