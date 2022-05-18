valor = int(input('digite o valor desejado: R$ '))
ced = 100
total=valor
totced=0
while True:
    if total >=ced:
        total-=ced
        totced+=1
    else:
        if totced > 0:
            print(f'print o total de cedulas de {ced} foram {totced}')
        if ced ==100:
            ced=50
        elif ced==50:
            ced=20
        elif ced==20:
            ced=10
        elif ced==10:
            ced=5
        elif ced==5:
            ced=2
        elif ced==2:
            ced=1
        totced=0
        if total==0:
            break
print('sua operaÇão foi encerrada ate mais!')


