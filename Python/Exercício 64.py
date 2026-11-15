n = int(input('''Digite um número inteiro!
[Digite 999 para encerrar] '''))
contador = soma = 0
while n != 999:
    contador += 1
    soma += n
    n = int(input('Digite um outro número inteiro! '))
print('Você digitou {} número(s) inteiro(s) e a soma entre eles é igual a {}.'.format(contador, soma))
