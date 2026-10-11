from random import randint
from time import sleep
itens = ('pedra', 'papel', 'tesoura')
pc = randint(0, 2)
print('''Jokenpô: Eu vou escolher entre pedra, papel ou tesoura...
E você? Qual você escolhe:
[0] pedra
[1] papel
[2] tesoura''')
escolha = int(input('Escolha: '))
print('Jo')
sleep(1)
print('ken')
sleep(1)
print('pô!')
sleep(1)
print('O computador escolheu {} e você escolheu {}...'.format(itens[pc], itens[escolha]))
if pc == 0:
    if escolha == 0:
        print('O jogo empatou!')
    elif escolha == 1:
        print('Papel embrulha pedra! Você ganhou!')
    elif escolha == 2:
        print('Pedra amassa tesoura! O computador ganhou!')
    else:
        print('Opção inválida! Tente novamente.')
elif pc == 1:
    if escolha == 0:
        print('Papel embrulha pedra! O computador ganhou!')
    elif escolha == 1:
        print('O jogo empatou!')
    elif escolha == 2:
        print('Tesoura corta papel! Você ganhou!')
    else:
        print('Opção inválida! Tente novamente.')
elif pc == 2:
    if escolha == 0:
        print('Pedra amassa tesoura! Você ganhou!')
    elif escolha == 1:
        print('Tesoura corta papel! O computador ganhou!')
    elif escolha == 2:
        print('O jogo empatou!')
    else:
        print('Opção invalida! Tente novamente.')
