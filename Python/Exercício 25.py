nome = str(input('Digite seu nome completo: ')).strip().upper()
print('Seu nome contém SILVA? {}{}{}'.format('\033[1;36m', 'SILVA' in nome, '\033[m'))
