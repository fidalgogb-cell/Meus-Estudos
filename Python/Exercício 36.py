c = float(input('Qual é o valor da casa? R$ '))
s = float(input('Qual é o salário do comprador? R$ '))
a = int(input('Em quantos anos você gostaria de financiar? '))
valor = c / (a * 12)
print('O valor da prestação será de R$ {:.2f}'.format(valor))
if valor <= s * 30 / 100:
    print('Empréstimo aprovado!')
else:
    print('Empréstimo negado!')
