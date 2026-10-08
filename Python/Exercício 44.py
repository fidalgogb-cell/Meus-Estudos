print('{:#^40}'.format(' LOJAS GUANABARA '))
valor = float(input('Qual é o valor das compras? R$ '))
print('''Escolha a forma de pagamento:
[1] À vista em dinheiro ou cheque.
[2] À vista no cartão.
[3] 2x no cartão.
[4] 3x ou mais no cartão.''')
escolha = int(input('Digite sua opção: '))
if escolha == 1:
    novo = valor - (valor * 10 / 100)
    print('Com 10% de desconto, a compra custará R$ {}'.format(novo))
elif escolha == 2:
    novo = valor - (valor * 5 / 100)
    print('Com 5% de desconto, a compra custará R$ {}'.format(novo))
elif escolha == 3:
    parcela = valor / 2
    print('A compra será parcelada em 2x de R$ {}, sem juros.'.format(parcela))
elif escolha == 4:
    novo = valor + (valor * 20 / 100)
    num = int(input('Quantas parcelas? '))
    parcela = novo / num
    print('Com 20% de juros, o produto custará R$ {} e sua compra será parcelada em {}x de R$ {:.2f}'.format(novo, num, parcela))
else:
    print('Opção inválida! Tente novamente.')
