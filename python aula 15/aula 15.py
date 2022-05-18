'''c=0
n=0
soma=0
while c<5:
    n = int(input('digte um numero: '))
    c+=1
    soma +=n
print(f'a soma foi de {soma}')
# essa nova forma pode ser utlizada no lugar do format'''

n=s=0
while True:
    n= int(input('digite um valor: '))
    if n ==999:
        break
    s+=n
print(f'a soma foi de {s}')