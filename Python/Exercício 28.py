from random import randint
from time import sleep
x = randint(1,5)
print('Vou pensar em um número entre 1 e 5...Tente adivinhar...')
y = int(input('Em qual número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if x==y:
    print('{}Você acertou!{}'.format('\033[1;32m', '\033[m'))
else:
    print('{}Você errou!{} Eu tinha pensado no número {}...'.format('\033[1;31m','\033[m', x))
print('Fim de jogo!')
