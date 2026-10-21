num = int(input('Digite um número inteiro: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('{}{}'.format('\033[34m', c), end=' ')
        total += 1
    else:
        print('{}{}'.format('\033[m', c), end=' ')
print()
print('{}O número {} foi divisível em {} ocorrência(s).'.format('\033[m', num, total))
if total == 2:
    print('E por isso é um número primo!')
else:
    print('E por isso não é um número primo!')
