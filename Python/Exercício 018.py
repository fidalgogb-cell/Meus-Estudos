from math import radians, sin, cos, tan
x = int(input('Digite um ângulo em graus: '))
r = radians(x)
print('O seno é {}{:.2f}{}, o cosseno é {}{:.2f}{} e a tangente é {}{:.2f}{}.'.format('\033[1;35m', sin(r), '\033[m', '\033[1;35m', cos(r), '\033[m', '\033[1;35m', tan(r), '\033[m'))
