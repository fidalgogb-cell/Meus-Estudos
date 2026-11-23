from random import randint
contador = 0
while True:
    escolha = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    jogador = int(input('Digite um número de 1 até 10: '))
    computador = randint(1, 10)
    print(f'O computador escolheu {computador}')
    resultado = jogador + computador
    if escolha == 'P' and resultado % 2 == 0:
        contador += 1
        print('Você ganhou! Próxima rodada...')
    elif escolha == 'I' and resultado % 2 != 0:
        contador += 1
        print('Você ganhou! Próxima rodada...')
    elif escolha == 'P' and resultado % 2 != 0 or escolha == 'I' and resultado % 2 == 0:
        break
print('Você perdeu! Fim de jogo!')
print(f'{contador} tentativas')
