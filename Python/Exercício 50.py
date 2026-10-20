soma = 0
contador = 0
for c in range (1, 7):
    x = int(input('Digite um número inteiro: '))
    if x % 2 == 0:
        soma += x
        contador += 1
print('Você informou {} número(s) par(es) e a soma é {}.'.format(contador, soma))
