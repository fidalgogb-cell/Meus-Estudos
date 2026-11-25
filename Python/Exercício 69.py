contador = 0
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [F/M] ')).strip().upper()[0]
    escolha = str(input('Deseja continuar cadastrando? [S/N] ')).strip().upper()[0]
    if idade > 18:
        contador += 1
    while escolha not in 'SN':
        escolha = str(input('Deseja continuar cadastrando? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break
print(f'Foram cadastradas {contador} pessoas com mais de 18 anos.')
