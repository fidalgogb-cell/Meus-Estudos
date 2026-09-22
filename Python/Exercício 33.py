a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
menor = a
if b<a and b<c:
    menor = b
if c < a and c < b:
    menor = c
print('{}{}{} é o menor valor.'.format('\033[1;36m', menor, '\033[m'))
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('{}{}{} é o maior valor.'.format('\033[1;33m', maior, '\033[m'))
