from random import randint
from time import sleep
x = randint(1,5)
print('Vou pensar em um número entre 1 e 5...Tente adivinhar...')
y = int(input('Em qual número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if x==y:
    print('Você acertou!')
else:
    print('Você errou! Eu tinha pensado no número {}...'.format(x))
print('Fim de jogo!')
