x = float(input('Qual é a distância da viagem em km? '))
if x <= 200:
    valor = x * 0.50
else:
    valor = x * 0.45
# valor = x * 0.50 if x <= 200 else x * 0.45
print('O valor da passagem será de {}R$ {:.2f}{}.'.format('\033[1;35m', valor, '\033[m'))
