'''frase = str(input('digite uma frase: ')).strip().upper() # strip é para tirar os espaços e upper é para deixar tudo maisculo
palavras = frase.split() #split vai dividir as palavras
junto = ''.join(palavras) # '' é para deixar sem o espaço
print('voce digitou a frase: {}'.format(junto))
inverso = ''
for letra in range(len(junto)-1, -1, -1): #utlizo o len do 'junto' somo com +1, começa com -1 para contar a primeira letra e outro -1 volta uma letra
    inverso +=junto[letra]
print(inverso)
if inverso == junto:
    print('é um palindromo')
else:
    print('nao é um palindromo')'''


frase = str(input('digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
print('voce digitou a frase: {}'.format(junto))
inverso = junto[::-1]
print('o inverso de {} é {}'.format(junto,inverso))
if inverso == junto:
    print('é um palindromo')
else:
    print('nao é um palindromo')











