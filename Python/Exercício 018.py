from math import radians, sin, cos, tan
x = int(input('Digite um ângulo em graus:'))
r = radians(x)
print('O seno é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}'.format(sin(r), cos(r), tan(r)))
