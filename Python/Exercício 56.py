somaidade = 0
maisvelho = 0
nomemaisvelho = ''
contador = 0
for pessoa in range(1, 5):
    nome = str(input('Digite o nome da {}ª pessoa: '.format(pessoa))).strip()
    idade = int(input('Digite a idade da {}ª pessoa: '.format(pessoa)))
    sexo = str(input('Sexo [F/M]: ')).strip().upper()
    somaidade += idade
    if sexo == 'M' and idade > maisvelho:
        maisvelho = idade
        nomemaisvelho = nome
    elif sexo == 'F' and idade < 20:
        contador += 1
media = somaidade / 4
print('A média de idade do grupo é de {} anos.'.format(media))
print('O homem mais velho do grupo se chama {} e tem {} anos.'.format(nomemaisvelho, maisvelho))
print('Existe(m) {} mulher(es) com menos de 20 anos no grupo.'.format(contador))
