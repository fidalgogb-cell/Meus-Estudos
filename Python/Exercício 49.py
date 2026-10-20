x = int(input('Digite um número inteiro: '))
print('{}'.format('*' * 20))
print('A tabuada de {} é:'.format(x))
for num in range (1, 11):
    mult = x * num
    print('{} x {} = {}'.format(x, num, mult))
print('{}'.format('*' * 20))
