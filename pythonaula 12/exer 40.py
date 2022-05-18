nome = str(input('nome do aluno:'))
n1 = float(input('nota 1:'))
n2 = float(input('nota 2: '))
m = (n1+n2)/2
print('a media do aluno {}, foi de: {}'.format(nome,m))
if m >=7: # posso utlizar o 'and' para colocar outras numerações
    print('o aluno {} esta aprovado!'.format(nome))
elif m<5:
    print('o aluno {} esta reprovado!'.format(nome))
elif 7 < m >=5:
    print('aluno {} esta de recuoeração'.format(nome))
