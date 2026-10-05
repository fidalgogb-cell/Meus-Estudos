from datetime import date
nascimento = int(input('Digite o ano de nascimento: '))
ano = date.today().year
idade = ano - nascimento
if idade <= 9:
    print('O(a) atleta tem {} ano(s) e pertence à categoria mirim.'.format(idade))
elif idade <= 14:
    print('O(a) atleta tem {} anos e pertence à categoria infantil.'.format(idade))
elif idade <= 19:
    print('O(a) atleta tem {} anos e pertence à categoria júnior.'.format(idade))
elif idade <= 25:
    print('O(a) atleta tem {} anos e pertence à categoria sênior.'.format(idade))
else:
    print('O(a) atleta tem {} anos e pertence à categoria master.'.format(idade))
