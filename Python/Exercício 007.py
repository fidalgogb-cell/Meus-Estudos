n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A média do(a) aluno(a) é {}{:.1f}{}.'.format('\033[1;34m', m, '\033[m'))
# {:.1f} arredonda para cima
