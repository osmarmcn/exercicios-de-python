# posso fazer um fatiamento, assim, não aparecer (0b = para binario / 0xd = para hexadecimal / 0o = para octal
# sendo ultizado aula 10 para o fatiamneto ex: após bin(num)[:2}))

num = int(input('digite um numero:'))
print('''escolha sua base para conversão:'
[1] converter para binario
[2] converter para hexadecimal
[3] converter para octal''')
opção = int(input('sua opção:'))
if opção == 1:
    print('{} o numero convertido para binario é: {}'.format(num,bin(num)[:2]))
elif opção ==2:
    print('{} o numero convertido para binario é: {}'.format(num,hex(num)))
elif opção == 3:
    print('{} o numero convertido para octal é: {}'.format(num, oct(num)))
else:
    print('numero invalido tente novamente!')
