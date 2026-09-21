s = float(input('Qual é o valor do salário? R$ '))
a = s * 15 / 100
s2 = s + a
print('Com 15% de aumento, o salário vai ficar {}R$ {:.2f}{}.'.format('\033[1;34m', s2, '\033[m'))
