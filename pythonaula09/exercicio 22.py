nome = str(input('digite um nome:')).strip()
print('seu nome é {}'.format(nome.upper()))
print('seu nome é {}'.format(nome.lower()))
print('o nome de {} possui {} letras'.format(nome, len(nome) - nome.count(' ')))
#print('o nome tem {} letras'.format(len(n)))
#print('seu primeiro nome possui {}'.format(nome.find(' '))) opção 1
separa = nome.split()
print('seu primeiro nome é {}, contendo, {} letras'.format(separa [0], len(separa [0])))
