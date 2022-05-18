L = float(input('largura:'))
A = float(input('altura:'))
area = L * A
print('sua parede possui uma dimessao de {} x {} sendo de {:.2f} metros quadrados'.format(L,A,area))
t = area/2
print('para pintar a parede serao necessarios {:.1f} litros de tinta'.format(t))