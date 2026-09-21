x = int(input('Digite um numero: '))
a = x * 2
b = x * 3
# c = x ** (1 / 2)
c = pow (x,(1 / 2))
print('O dobro de {} é {}{}{}.'.format(x, '\033[1;34m', a, '\033[m'))
print('O triplo de {} é {}{}{}.'.format(x,'\033[1;34m', b, ' \033[m'))
print('A raiz quadrada de {} é {}{:.2f}{}.'.format(x, '\033[1;34m', c, ' \033[m'))
