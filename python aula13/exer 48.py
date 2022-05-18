from time import sleep
s =0
cont=0
for c in range (1,501, 2):
    if c % 3 ==0:
        cont= cont+1
        s=s+c
        print(c)
print('a soma de dos multplos de tres:{}'.format(s))
print('foram apresentados {} numeros'.format(cont))
print('fim')