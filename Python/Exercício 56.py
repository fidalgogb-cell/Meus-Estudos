somaidade = 0
maisvelho = 0
nomemaisvelho = ''
contador = 0
for pessoa in range(1, 5):
    nome = str(input('Digite o nome da {}ª pessoa: '.format(pessoa)))
    idade = int(input('Digite a idade da {}ª pessoa: '.format(pessoa)))
    sexo = int(input('''Qual é o seu sexo?
    [1] Feminino
    [2] Masculino
    Sua escolha: '''))
    somaidade += idade
    if sexo == 2 and idade > maisvelho:
        maisvelho = idade
        nomemaisvelho = nome
    elif sexo == 1 and idade < 20:
        contador += 1
media = somaidade / 4
print('A média de idade do grupo é de {} anos.'.format(media))
print('O homem mais velho do grupo se chama {} e tem {} anos.'.format(nomemaisvelho, maisvelho))
print('Existe(m) {} mulher(es) com menos de 20 anos no grupo.'.format(contador))
