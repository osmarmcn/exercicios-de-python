'''c=1
n=0
s=0
while c > 0:
    n = int(input('digite um numero: '))
    if n == 999:
        break
    s+=n
    c+=1
print(f'foram contados {c} e soma foi de {s}')'''

c=0
n=0
s=0
while True:
    n=int(input('digite um numero(para parar 999): '))
    if n ==999:
        break
    c+=1
    s+=n
print(f'foram contados {c} e sua soma foi de {s}')
