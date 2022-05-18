'''print('\033[0;32;41molá mundo!\033[m')
print('\033[1;36;47mvamos curtir o revellion!!!\033[m')
print('\033[7;34m hoje é dia de festa\033[m')'''

'''a = 5
b = 3
print('eu tenho \033[7;31m{}\033[m reais e ele \033[7;36m{}\033[m reais'.format(a,b))'''

'''print('\033[4;41mhoje estou feliz!!\033[m')'''

'''n1 = 'lucas'
n2 = 'osmar'
print('\033[7;35m{} e {}\033[m foram para a festa.'.format(n1,n2))'''

'''nome = 'osmar'
print('vamos passar a virada do ano juntos {}{}{}'.format('\033[7;36m',nome, '\033[m'))'''

nome = 'Osmar'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print('vamos sair para alguma praia {}{}{}'.format(cores['amarelo'], nome, cores['amarelo']))