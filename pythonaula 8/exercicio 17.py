import math
c1 = int(input('cateto adjacente vale:'))
c2 = int(input('cateto oposto vale:'))
h = math.hypot(c1,c2)
print ('cateto adjacente vale {} ja o oposto {} tendo sua hipotenusa {:.2f}'.format(c1,c2,h))
