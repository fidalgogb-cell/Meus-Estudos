somaidade = 0
for pessoa in range(1, 5):
    # nome = str(input('Digite o nome da {}ª pessoa: '.format(pessoa)))
    idade = int(input('Digite a idade da {}ª pessoa: '.format(pessoa)))
    # sexo = str(input('Digite o sexo da {}ª pessoa: '.format(pessoa)))
    somaidade += idade
media = somaidade / 4
print('A média de idade do grupo é de {} anos.'.format(media))
