nome = str(input('qual seu nome? '))
v = float(input('qual valor do imovel (R$): '))
sal = float(input('qual seu salario(R$): '))
tem = int(input('quantos anos deseja pagar o imovel: '))
parcela = v/(tem*12)
minimo = (sal*30/100)
print('você {}, tera que pagar por mês R$: {:.2f} '.format(nome,parcela))
print('comapraçâo {} - {:.2f} '.format(sal,minimo))
if parcela <= minimo:
    print('emprestimo aprovado')
else:
    print('emprestimo negado')