km = float (input('quantos km rodados?'))
a = int(input('quantos dias o carro ficou alugado?'))
d = (60*a) + (km*0.15)
print('o carro pecorreu {}km, sendo alugado por {} dias, contendo seu valor do aluguel de R${:.2f}'.format(km,a,d))



