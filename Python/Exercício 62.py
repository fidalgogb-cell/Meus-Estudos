n1 = int(input('Digite o primeiro termo de uma progressão aritmética: '))
r = int(input('Digite a razão de uma progressão aritmética: '))
termo = n1
contador  = 1
total = 0
mais = 10
print('Os 10 primeiros termos dessa progressão aritmética são: ')
while mais != 0:
    total = total + mais
    while contador <= total:
        print('{}'.format(termo), end=' ')
        termo += r
        contador += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão aritmética foi finalizada com {} termos mostrados.'.format(total))
