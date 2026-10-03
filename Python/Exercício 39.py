from datetime import date
nascimento = int(input('Digite o ano de nascimento: '))
atual = date.today().year
idade = atual - nascimento
print('Quem nasceu em {} completa {} ano(s) em {}.'.format(nascimento, idade, atual))
if idade < 18:
    saldo = 18 - idade
    print('Faltam {} ano(s) para o alistamento.'.format(saldo))
    alistamento = atual + saldo
    print('Seu alistamento será em {}.'.format(alistamento))
elif idade == 18:
    print('Você tem que se alistar imediatamente!')
else:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} ano(s).'.format(saldo))
    alistamento = atual - saldo
    print('Seu alistamento foi em {}.'.format(alistamento))
