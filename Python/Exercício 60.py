# from math import factorial
# x = int(input('Digite um número para calcular o seu fatorial: '))
# f = factorial(x)
# print('O fatorial de {} é igual a {}.'.format(x, f))

x = int(input('Digite um número para calcular o seu fatorial: '))
multiplicar = 1
print('Calculando o fatorial de {}! ='.format(x), end=' ')
while x > 0:
    print('{}'.format(x), end=' ')
    print('x' if x > 1 else '=', end=' ')
    multiplicar *= x
    x -= 1
print('{}'.format(multiplicar))

# x = int(input('Digite um número para calcular o seu fatorial: '))
# multiplicar = 1
# for c in range(1, x + 1):
#    multiplicar *= c
# print('{}! = {}'.format(x, multiplicar))'''
