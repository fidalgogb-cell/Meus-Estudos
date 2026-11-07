x = int(input('Digite um valor: '))
y = int(input('Digite outro valor: '))
escolha = int(input('''Menu: 
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos numeros
[5] Sair do programa
Escolha uma das opções: '''))
if escolha == 1:
    somar = x + y
    print('{} + {} = {}'.format(x, y, somar))
elif escolha == 2:
    multiplicar = x * y
    print('{} x {} = {}'.format(x, y, multiplicar))
