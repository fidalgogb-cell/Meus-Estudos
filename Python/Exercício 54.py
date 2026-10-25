from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for pessoa in range(1, 8):
    nascimento = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(pessoa)))
    if atual - nascimento >= 21:
        totalmaior += 1
    else:
        totalmenor += 1
print('Número de pessoas que já são maiores de 21 anos: {}'.format(totalmaior))
print('Número de pessoas que ainda não atingiram a maioridade: {}'.format(totalmenor))
