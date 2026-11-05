from random import randint
x = randint(0,10)
print('Vou pensar em um número entre 0 e 10...Tente adivinhar...')
acertou = False
contador = 0
while not acertou:
    y = int(input('Em qual número eu pensei? '))
    contador += 1
    if x == y:
        acertou = True
    else:
        if y < x:
            print('Mais... Tente novamente!')
        elif y > x:
            print('Menos... Tente novamente!')
print('Você acertou com {} tentativa(s)!'.format(contador))
