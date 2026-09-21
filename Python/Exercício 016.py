# import math
# x = float(input('Digite um número real: '))
# print('O valor inteiro é: {}.'.format(math.trunc(x)))

from math import trunc
x = float(input('Digite um número real: '))
print('O valor inteiro é: {}{}{}.'.format('\033[1;35m', trunc(x), '\033[m'))

# x = float(input('Digite um número real: '))
# print('O valor inteiro é: {}.'.format(int(x)))
