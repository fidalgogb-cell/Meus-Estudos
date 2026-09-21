x = int(input('Digite um número inteiro: '))
y = x + 1
z = x - 1
print('O sucessor de {} é {}{}{}.'.format(x, '\033[1;34m', y, '\033[m'))
print('O antecessor de {} é {}{}{}.'.format(x, '\033[1;34m', z, '\033[m'))
