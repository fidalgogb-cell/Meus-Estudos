from random import choice
a = input('Digite o primeiro nome: ')
b = input('Digite o segundo nome: ')
c = input('Digite o terceiro nome: ')
d = input('Digite o quarto nome: ')
print('O nome sorteado foi {}{}{}.'.format('\033[1;35m', choice([a,b,c,d]), '\033[m'))
