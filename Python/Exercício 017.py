# from math import sqrt
# ca = float(input('Digite o valor do cateto adjacente:'))
# co = float(input('Digite o valor do cateto oposto:'))
# hi = sqrt(ca**2+co**2)
# print('A hipotenusa vale {:.2f}'.format(hi))

from math import hypot
ca = float(input('Digite o valor do cateto adjacente:'))
co = float(input('Digite o valor do cateto oposto:'))
hi = hypot(ca,co)
print('A hipotenusa vale {:.2f}'.format(hi))
