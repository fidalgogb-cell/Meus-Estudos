p = float(input('Qual é o preço do produto? R$'))
d = p*5/100
p2 = p-d
print('Com 5% de desconto, o produto passará a custar R${:.2f}'.format(p2))
