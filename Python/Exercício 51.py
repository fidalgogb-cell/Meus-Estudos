x = int(input('Digite o primeiro termo de uma progressão aritmética: '))
y = int(input('Digite a razão de uma progressão aritmética: '))
# z é igual ao décimo termo de uma progressão aritmética
z = x + (10 - 1) * y
print('Os 10 primeiros termos dessa progressão aritmética são: ')
for c in range (x, z + y, y):
     print('{}'.format(c), end=' > ')
print('ACABOU')
