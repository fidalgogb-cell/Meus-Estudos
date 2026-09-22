nome = str(input('Digite seu nome completo: ')).strip()
lista = nome.split()
print('Seu primeiro nome é {}{}{}.'.format('\033[1;36m', lista[0], '\033[m'))
print('Seu último nome é {}{}{}.'.format('\033[1;36m', lista[len(lista) - 1], '\033[m'))
