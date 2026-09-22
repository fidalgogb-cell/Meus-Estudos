from datetime import date
ano = int(input('Qual ano você quer analisar? Digite {}0{} para o ano atual: '.format('\033[1;31m', '\033[m')))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {}{}{} é bissexto.'.format('\033[1;32m', ano, '\033[m'))
else:
    print('O ano {}{}{} não é bissexto.'.format('\033[1;32m', ano, '\033[m'))
