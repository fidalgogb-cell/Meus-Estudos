x = float(input('Digite seu salário em R$ '))
if x <= 1250:
    y = x + x * 15 / 100
else:
    y = x + x * 10 / 100
print('Seu salário com aumento será {}R$ {:.2f}{}.'.format('\033[1;32m', y, '\033[m'))
