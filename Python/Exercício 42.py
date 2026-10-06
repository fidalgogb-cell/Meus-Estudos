r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É possivel formar um triângulo', end=' ')
    if r1 == r2 == r3:
        print('equilátero: todos os lados são iguais.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('isósceles: dois lados são iguais.')
    else:
        # r1 != r2 != r3 != r1
        print('escaleno: todos os lados são diferentes.')
else:
    print('Não é possivel formar um triângulo.')
