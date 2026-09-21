r = float(input('Digite um valor em R$ '))
# 1 dólar equivale a 3.27 reais
d = r/5.13
print('R$ {} equivalem a {}{:.2f} dólares{}.'.format(r, '\033[1;34m', d, '\033[m'))
