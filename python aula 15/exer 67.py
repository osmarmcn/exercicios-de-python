from time import sleep
while True:
    n= int(input('digite um valor: '))
    if n < 0:
        break
        print(f'processo finalizado!')
    for c in range(1,11):
        tabuada = n*c
        print(f' {n} x {c} = {tabuada}' )
        sleep(0.5)

