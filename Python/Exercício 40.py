nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print('A média do(a) aluno(a) foi {:.1f}'.format(media))
if media < 5:
    print('Aluno(a) reprovado(a)!')
elif 5 <= media <= 6.9:
    print('Aluno(a) em recuperação!')
else:
    print('Aluno(a) aprovado(a)!')
