n1 = int(input('Digite o primeiro termo de uma progressão aritmética: '))
r = int(input('Digite a razão de uma progressão aritmética: '))
termo = n1
contador  = 1
print('Os 10 primeiros termos dessa progressão aritmética são: ')
while contador <= 10:
    print('{}'.format(termo), end=' ')
    termo += r
    contador += 1
print('ACABOU')
