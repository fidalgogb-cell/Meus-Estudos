c = float(input('Digite a temperatura em C°: '))
f = c * 9 / 5 + 32
print('{} C° equivalem a {}{} F°{}.'.format(c, '\033[1;34m', f, '\033[m'))
# Não precisa de () na conta por causa da ordem de precedência
