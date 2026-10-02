num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] Binário
[2] Octal
[3] Hexadecimal''')
escolha = int(input('Sua escolha: '))
if escolha == 1:
    print('{} em decimal corresponde a {} em binário.'.format(num, bin(num)[2:]))
elif escolha == 2:
    print('{} em decimal corresponde a {} em octal.'.format(num, oct(num)[2:]))
elif escolha == 3:
    print('{} em decimal corresponde a {} em hexadecimal.'.format(num, hex(num)[2:]))
else:
    print('Opção inválida! Tente novamente.')
