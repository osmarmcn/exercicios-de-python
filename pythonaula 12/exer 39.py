nome = str(input('qual seu nome: '))
nasc = int(input('que ano você nasceu:'))
atual = int(input('que ano estamos hoje: '))
alist = atual - nasc
if alist== 18:
    print('você esta no periodo de alistamento!Sr.{}'.format(nome))
elif alist < 18:
    saldo = 18 - alist
    print("ainda não está apto para o alistamento, sr.{}, faltando {} ano(s)".format(nome,saldo))
    ano = atual + saldo
    print("seu ano de alsitamento é: {}".format(ano))
else:
    saldo = alist - 18
    print('você passou do periodo de alistamento. Sr.{},sendo ultrapassado {} ano(s)'.format(nome,saldo))
    ano = atual - saldo
    print('você era para ter se alsitado no ano de {}'.format(ano))
