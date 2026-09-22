n = int(input('Digite um número qualaquer: '))
resultado = n % 2
if resultado == 0:
    print('O número {}{}{} é par.'.format('\033[1;33m', n, '\033[m'))
else:
    print('O número {}{}{} é ímpar.'.format('\033[1;33m', n, '\033[m'))
