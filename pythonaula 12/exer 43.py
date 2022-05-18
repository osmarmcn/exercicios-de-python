nome = str(input('digite seu nome:'))
peso = float(input('digite seu peso (kg): '))
altura = float(input('digite sua altura (M): '))
imc = peso/(altura**2)
print('seu imc {}, foi de {:.2f}'.format(nome,imc))
if imc < 18.5:
    print('{}, você esta abaixo do peso ideal'.format(nome))
elif imc > 18.5 and imc < 25:
    print('{}, seu peso esta dentro do ideal'.format(nome))
elif imc > 25 and imc <30:
    print('{}, você esta acima do peso'.format(nome))
elif imc >30 and imc <35:
    print('{}, você esta com sobrepeso'.format(nome))
elif imc > 35: # quando colcocar else nao necessita colocar imc >35
    print('você esta com obesidade morbida')
