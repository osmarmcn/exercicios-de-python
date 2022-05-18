'''km = int(input('foi pecorrido quantos km:'))
if km <=200:
    pc = km * 0.50
    print('foi pecorrido {} km,sendo o custo da passagem de R$ {:.2f}'.format(km,pc))
else:
    pl = km * 0.45
    print('foi pecorrido {} km, sendo o custo da passgem de R$ {:.2f}'.format(km, pl))'''


km = float(input('sua viagem vai ser de quantos km?:'))
print('sua viagem vai ter um percurso de {} km'.format(km))
preço = km * 0.50 if km <=200 else distancia de km * 0.45 #esta apresetnado erro o programa
print('o valor da passagem vai ficar {:.2f}'.format(preço))