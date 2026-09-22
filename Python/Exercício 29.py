x = float(input('Qual é a velocidade atual do carro? '))
if x > 80:
    print('{}Você foi multado!{} O limite permitido é de 80km/h.'.format('\033[1;31m', '\033[m'))
    multa = (x - 80) * 7
    print('Você deve pagar uma multa de {}R$ {:.2f}{}.'.format('\033[1;31m', multa, '\033[m'))
print('{}Tenha um bom dia! Dirija com segurança!{}'.format('\033[1;34m', '\033[m'))
