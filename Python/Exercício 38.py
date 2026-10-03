x = int(input('Digite o primeiro número: '))
y = int(input('Digite o segundo número: '))
if x > y:
    print('{} é maior que {}.'.format(x, y))
elif y > x:
    print('{} é maior que {}.'.format(y, x))
else:
    print('Os números digitados são iguais.')
