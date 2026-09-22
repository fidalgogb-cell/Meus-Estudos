num = int(input('Digite um número de 0 até 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}{}{}'.format('\033[1;36m', u, '\033[m'))
print('Dezena: {}{}{}'.format('\033[1;36m', d, '\033[m'))
print('Centena: {}{}{}'.format('\033[1;36m', c, '\033[m'))
print('Milhar: {}{}{}'.format('\033[1;36m', m, '\033[m'))
