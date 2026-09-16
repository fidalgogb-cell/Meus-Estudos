x = float(input('Qual é a velocidade atual do carro? '))
if x > 80:
    print('Você foi multado! O limite permitido é de 80km/h')
    multa = (x - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
