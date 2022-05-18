'''import math
n = int(input('digite o angulo:'))
s = math.sin(math.radians(n))
c= math.cos(math.radians(n))
t = math.tan(math.radians(n))
print('o seno de {} vale {:.2f}, ja o coseno {} vale {:.2f} e sua tangente {:.2f}'.format(n,s,n,c,t))'''

from math import radians,sin,cos,tan
n = int(input('digite um angulo:'))
s = sin(radians(n))
print('o seno de {} vale {}'.format(n,s))
c = cos(radians(n))
print('o cosseno de {} vale {}'.format(n,c))
t = tan(radians(n))
print ('a tagente de {} vale {}'.format(n,t))