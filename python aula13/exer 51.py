primeiro = int(input('digite um numero:'))
razao = int(input('digite a razao: '))
dec = primeiro + (10-1) * razao
for c in range(primeiro,dec+razao, razao):
    print(c)
