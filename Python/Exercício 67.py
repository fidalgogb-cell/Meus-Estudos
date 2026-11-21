while True:
    num = int(input('''Digite um número para mostrar a sua tabuada...
[Para encerrar: Digite um número negativo] → '''))
    print('~' * 50)
    if num < 0:
        break
    for c in range(1, 11):
        result = num * c
        print(f'{num} x {c} = {result}')
    print('~' * 50)
print('FIM!')
