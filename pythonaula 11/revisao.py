'''a = (5+9+4*8)/2
b = (8+3+5+6*6)/4
s = a+b
print('a soma de {} e {} é igual {}'.format(a,b,s))'''

'''a = 9//2
print('o resto da divisão é',a)
b = 9% 2
print(' a divisao interira é',b)
c = 9**5
print('a potencia de 9 é',c)'''

'''num = input('digite um numero:')
print('é uma letra:',num.isnumeric())
print('é um numero:',num.isdecimal())
print('é str:',num.isalnum())
print('é o que:',num.isalpha())
print('qual o tipo:',type(num))
print('teme espaços:',num.isspace())
print('tem letra:',num.isalpha())'''

'''num = int(input('digite um numero:'))
a1 = num + 1
a2 = num - 1
print('o numero {} tem como sucessor {} e seu antecessor {}.'.format(num,a1,a2))'''

'''num = int(input('digite um numero:'))
a1 = num * 2
a2 = num * 3
a3 = num ** 2
a4 = num ** 3
a5 = num ** (1/2)
a6 = num + 10
a7 = num - 10
a8 = num % 2
a9 = num// 2
print('o dobro de {} é {}'.format(num,a1))
print('o triplo de {} é {}'.format(num,a2))
print('a potencia de {} é {}'.format(num,a3))
print('o cubo de {} é {}'.format(num,a4))
print('a raiz de {} é {}'.format(num,a5))
print('a soma de {} é {}'.format(num,a6))
print('a diminuiÇão de {} é {}'.format(num,a7))
print('a divisao inteira de {} é {}'.format(num,a8))
print('o resto da divisao de {} é {}'.format(num,a9))'''

'''a1 = 20
a2 = 30
a3 = 40
a4 = 50
m = (a1+a2+a3+a4)/4
print('a media é:{}'.format(m))'''
'''n1 = float(input('digite um numero:'))
n2 = float(input('digite um numero:'))
n3 = float(input('digite um numero:'))
m =(n1+n2+n3)/3
print('a media é: {:.2f}'.format(m))'''

'''num = int(input('digite o valor em metros:'))
km = num/1000
hcm = num/100
dm = num/10
dcm = num*10
cm = num*100
mm = num*1000
print('o valor km :{} \n o valor em hcm: {}\n valor de dm:{}\n o valor em dcm: {} \n o valor em cm é:{} \n valor em mm é: {}'.format(km,hcm,dm,dcm,cm,mm))'''

'''num = int(input('a tubuada de:'))
a1 = 1 * num
a2 = 2 * num
a3 = 3 * num
a4 = 4 * num
a5 = 5 * num
print(' 1 x {} = {} \n 2 x {} = {} \n 3 x {} = {} \n 4 x {} = {} \n 5 x {} = {}'.format(num,a1,num,a2,num,a3,num,a4,num,a5))'''

'''valor = float(input('valor dolar hoje:'))
tenho = float(input('hoje tenho R$:'))
conversao = tenho/valor
print('1 dolar custa {}, contudo, quero comprar {} dolares com dinheiro que tenho'.format(valor, conversao))'''

'''largura = float(input('a largura da parede:'))
altura = float(input('altura da parede:'))
area = largura * altura
p = area/2
print('area da parede em questão de {:.2f} metros quadrados sendo necessario {:.2f} litros de tinta'.format(area,p))'''

'''produto = float(input('um produto custa R$:'))
desconto = produto - (produto*5/100)
print('o produto custa R$ {} com desconto fica R$ {}'.format(produto,desconto))'''

'''salario = float(input('o salrio do fucionario R$:'))
reajsute = salario + (salario*15/100)
print('o salario atual é de R$ {}, com reajuste fica R$ {}'.format(salario,reajsute))'''

'''km = int(input('\033[7;32mquantos km foi pecorrido com o carro?\033[m'))
dias = int(input('\033[1;33mquantos dias ficou com o carro?'))
n1 = dias * 60
n2 = km * 0.15
s = n1 +n2
print('\033[4;34mo custo do carro neste perido que foi aludao é de R$ {}'.format(s))
print('\033[4;35m cada dia custou R$ {} com o percurso feito {} KM apresetando o valor de R$ {}'.format(n1,n2,s))'''

'''import math
num = float(input('digite um numero:'))
print('a parte inteira do numero {} é de {}'.format(num,math.trunc(num)))'''

'''from math import radians,cos,tan,sin
angulo = int(input('digite um angulo:'))
print('o seno de {} é {:.2f}'.format(angulo,cos(radians(angulo))))
print('o coseno de {} é {:.2f}'.format(angulo,sin(radians(angulo))))
print('a tangente de {} é {:.2f}'.format(angulo,tan(radians(angulo))))'''

'''import math
angulo = int(input('digite o angulo:'))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print('o seno de {} é {:.2f} \n o coseno de {} é {:.2f} \n a tangente {} é {:.2f} '.format(angulo,sen,angulo,cos,angulo,tan))'''

'''ca = int(input('qual comprimento do cateto adjacente:'))
co = int(input('qual o comprimento do cateto adjacente:'))
n1 = ca**2
n2 = co**2
H = (n1 + n2)**(1/2)
print('o valor da hipotenusa {:.2f}'.format(H))'''

'''import random
n1 = str(input('escolha um nome:'))
n2 = str(input('escolha um  nome:'))
n3 = str(input('escolha um nome:'))
n4 = str(input('escolha um nome:'))
lista = [n1,n2,n3,n4]
escolha = random.choice(lista)
print('o nome escolhido foi {}'.format(escolha))'''

'''from random import shuffle
n1 = int(input('digite um numero:'))
n2 = int(input('digite um numero:'))
lista = [n1,n2]
shuffle(lista)
print('o numero em ordem é {}'.format(lista))'''

'''import random
random.randint(0,10)

print('o numero escolhido foi {}'.format(random.randint(0,10)))'''

'''from random import sample #necessito utliza de uma forma melhor
n1 = int(input('digite um numero:'))
n2 = int(input('digite um numero:'))
n3 = int(input('digite um numero:'))
lista = [n1,n2,n3]
embaralha = sample(lista,len(lista))
print(embaralha)'''

'''from playsound import playsound # esta dando erro 
playsound('/patch/to/ex21.mp3')
print('playing sound using playsound')'''

'''nome = str(input('digite um nome:')).strip()
print('o nome com letra maiuscula fica assim: {}'.format(nome.upper()))
print('o nome com letra minuscula fica assim: {}'.format(nome.lower()))
print('qauntas letras {}, possuindo {} letras'.format(nome, len(nome) - nome.count(' ')))
print('o nome {} possui em sua primeira palavra {} letras'.format(nome, nome.find(' ')))'''

'''nome = str(input('digite o nome:\033[1;34'))
print('quantas letras A tem no nome:{} '.format(nome.count('a')))
print('substituição: {}'.format(nome.replace('mendes','jose')))
print(' tem a palavra {}'.format(nome.find('osmar')))
print(nome[0:15:3])'''

'''from random import randint
n = int(input('pensei nesse numero:'))
num = randint(0,3)
if n == num:
    print('você acertou o numero, Parabéns!!')
else:
    print('voce errou!! pensei no numero {} e nao no {}'.format(n,num))'''

'''vel = float(input('qual sua velocidade:'))
if vel >=80:
    print('infelizmente voce ultrpassou o limite de velocidade, estava {} km/h'.format(vel))
else:
    print('voce estava dentro dos limites')'''

'''num = int(input('digite um numero:'))
resto = num % 2
if resto == 0:
    print('é par')
else:
    print('é impar')'''

'''from math import trunc
num=1
while num !=0:
    num = float(input('digite um numero: '))
    n=trunc(num)
    print(trunc(num))
print('fim')'''

'''from math import sin,cos,tan,radians
angulo= int(input('digite o angulo: '))
print('o seno de {} é {:.2f}'.format(angulo,sin(radians(angulo))))
print('o coseno de {} é {:.2f}'.format(angulo,cos(radians(angulo))))
print('o tangente de {} é {:.2f}'.format(angulo,tan(radians(angulo))))'''


'''from random import choice
for lista in range (1,3):
    n1 = str(input('nome do aluno: '))
    n2= str(input('nome do outro aluno: '))
    n3= str(input('nome de outro aluno:'))
    lista= [n1,n2,n3]
    escolha= choice(lista)
    print('o aluno escolhido foi {}'.format(escolha))'''

'''from random import shuffle
n1= str(input('nome do aluno: '))
n2= str(input('nome de outro aluno: '))
n3= str(input('nome do ultimo aluno: '))
lista= [n1,n2,n3]
escolha = shuffle(lista)
print('a ordem de apresentação é {}'.format(lista))'''

'''from math import hypot
ca= float(input('digite um valor: '))
co= float(input('digte outro valor: '))
#hi = (ca**2 + co**2)**(1/2)
hi= hypot(ca,co)
print('o valor da hipotenusa corresponde {:.2f}'.format(hi))'''

'''frase = str(input('digite: '))
print(frase.count('a'))
print(len(frase))
print(frase.replace('viajar', 'amar'))
print(frase.find('amar'))
print(frase.title()) #primeira letra sempre maiuscula
print(frase.lower())
print(frase.upper())
print(len(frase))'''

'''frase = str(input('digite uma frase: ')).strip()
print('a frase com letra maiuscula {}'.format(frase.upper()))
print('a frase com letra minuscula {}'.format(frase.lower()))
print('a frase com as iniciais maiuscula {}'.format(frase.title()))
print('total de letras da frase foi de {}'.format(len(frase) - frase.count(' '))) # o count vai contar quantos espaços tem entre as palavras da frase
#print('primeira palavra é {} e possui {} letras'.format(frase.find(' ')) # esse espaço busca saber a primeira palavra
separa= frase.split()# o split vai fazer uma lista dos nomes ali feitos
print('seu primeiro nome é {} e possui {} letras'.format(separa[0], len(separa[0])))'''
# o len é para ler a quantidade de letras do primeiro nome

'''num = int(input('digite um valor: '))
u = num // 1 % 10
d = num // 10 % 10
c= num // 100 % 10
m = num // 1000 % 10
print('o numero  {}'.format(num))
print('a unidade é {}'.format(u))
print('a dezena é {}'.format(d))
print('centena é {}'.format(c))
print(' a milhar do numero {}'.format(m))'''

'''for cidade in range(0,3):
    cidade = str(input('qual sua cidade: '))
    print(cidade[:5].upper() == 'SANTO')'''

'''while True:
    nome = str(input('qual seu nome: '))
    print('seu nome tem silva? {}'.format('SILVA' in nome.upper()))'''

'''frase = str(input('qual a frase: ')).upper().strip()
print('quanta vezes aparece a letra {}'.format(frase.count('A')))
print('onde apareceu a primeira letra {}'.format(frase.find('A')+1))
print('a ultima letra A apareceu {}'.format(frase.rfind('A')+1))'''


'''from random import randint
computador = randint(1,5)
print('escolhi um numero tente adivinhar')
jogador = int(input('escolha um numero: '))
if jogador == computador:
    print('parabens voce acertou')
else:
    print('continue tentando eu escolhi {} e voce {}'.format(jogador,computador))'''

'''velocidade = float(input('velocidade de momento km/h: '))
multa = (velocidade-80)*7
if velocidade > 80:
    print('voce foi multado por exceder a velocidade permtida')
    print('sua multa foi de R$ {}'.format(multa))
else:
    print('voce esta dentro do limite de velocidade permitida')'''
'''tp=0
ti=0
for n in range(1,5):
    n= int(input('digite um valor: '))
    if n % 2==0:
        print('o numero é par')
        tp+=1
    else:
        print('o numero é impar')
        ti+=1
    print('o total de numeros pares {} e impares {}'.format(tp,ti))'''

'''km = float(input('qual distancia de sua viagem? '))
if km <= 200:
    preço= km * 0.5
else:
    preço = km * 0.45
print(f'o valor da passagem será de R${preço}')'''

'''from datetime import date # esta dando uma repetição infinita
ano = int(input('qual ano você deseja saber: '))
if ano ==0:
    ano = date.today().year
if ano % 4==0 and ano % 100 !=0 or ano % 400==0:
    print('ano é bissexto')
else:
    print('o ano não é bissexto')'''

'''for c in range (1,5):
    n1 = int(input('digite um valor: '))
    n2= int(input('digte um valor: '))
    n3= int(input('digite um valor: '))
    maior=n1
    if n2 > n1 and n2 > n3:
        maior =n2
    if n3 > n1 and n3 > n2:
        maior=n3
    menor = n1
    if n2 < n1 and n2 < n3:
        menor=n2
    if n3 < n2 and n3 < n1:
        menor=n3
print(f'o maior numero digitado foi {maior}')
print(f'o menor numero digitado foi {menor}')'''

'''nome = str(input('nome do funcionario: '))
sal = float(input('qual seu salario R$: '))
if sal > 1250:
    reajuste = sal + (sal*10/100)
    print(escolha uma opção:
    [1] vale transporte
    [2] plano de saude 
    [3] vale alimentação)
    opção= int(input('escolha sua opção: '))
    if opção ==1:
        saln= reajuste + 300
    elif opção == 2:
        saln= reajuste - (reajuste*5/100)
    elif opção ==3:
        saln= reajuste + (reajuste*7/100)
else:
    reajuste= sal + (sal*15/100)
print(f'o rejsute do salari do funcionario {nome} foi de {reajuste}')
print(f' o funcionario escolheu {opção},, com seu novo salario {saln}')'''

c1 = int(input('comprimento do lado 1: '))
c2 = int(input('comprimento do lado 2: '))
c3 = int(input('comprimento do lado 3: '))
if c1 < c2+c3 and c2<c1+c3 and c3<c2+c1:
    print('podem forma um triangulo')
else:
    print('nao podem forma um triangulo')








''