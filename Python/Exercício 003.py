n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
cores = {'roxo':'\033[1;35m', 'limpa':'\033[m'}
print('A soma entre {}{}{} e {}{}{} é igual a {}{}{}.'.format(cores['roxo'], n1, cores['limpa'], cores['roxo'], n2, cores['limpa'], cores['roxo'], s, cores['limpa']))
