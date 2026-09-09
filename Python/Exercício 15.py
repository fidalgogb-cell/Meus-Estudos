d = int(input('Quantos dias o carro ficou alugado?'))
q = float(input('Qual foi a quantidade de kilômetros percorridos?'))
# 60 reais por dia e 0.15 reais por kilômetro
t = (d*60)+(q*0.15)
print('O valor total a pagar é de {:.2f} reais'.format(t))
