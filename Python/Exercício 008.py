x = float(input('Digite um valor em metros: '))
a = x * 100
b = x * 1000
c = x / 1000
print('O valor de {} metros equivale a {}{:.0f}{} centímetros, {}{:.0f}{} milímetros'.format(x,'\033[1;34m', a, '\033[m', '\033[1;34m', b, '\033[m'),end= ' ')
# {:.0f} mostra como se fosse um número inteiro
print('e {}{:.0f}{} kilômetros.'.format('\033[1;34m', c, ' \033[m'))
