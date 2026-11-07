from time import sleep
x = int(input('Digite um valor: '))
y = int(input('Digite outro valor: '))
escolha = 0
while escolha != 5:
    print('''Menu: 
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos valores
    [5] Sair do programa''')
    escolha = int(input('Escolha uma das opções: '))
    if escolha == 1:
        somar = x + y
        print('{} + {} = {}'.format(x, y, somar))
    elif escolha == 2:
        multiplicar = x * y
        print('{} x {} = {}'.format(x, y, multiplicar))
    elif escolha == 3:
        if x > y:
            maior = x
            print('{} > {}'.format(x, y))
        elif y > x:
            maior = y
            print('{} > {}'.format(y, x))
        else:
            print('{} = {}'.format(x, y))
    elif escolha == 4:
        x = int(input('Digite um valor: '))
        y = int(input('Digite outro valor: '))
    elif escolha == 5:
        print('Finalizando...')
        sleep(2)
    else:
        print('Opção inválida! Tente novamente!')
print('Volte sempre!')
