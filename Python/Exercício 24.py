cidade = str(input('Digite o nome de uma cidade: ')).strip().upper()
print('Sua cidade começa com a palavra SANTO? {}{}{}'.format('\033[1;36m', cidade[:5] == 'SANTO', '\033[m'))
