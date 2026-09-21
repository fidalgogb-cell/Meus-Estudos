d = int(input('Quantos dias o carro ficou alugado? '))
q = float(input('Qual foi a quantidade de km percorridos? '))
# R$ 60 por dia e R$ 0.15 por km
t = (d * 60) + (q * 0.15)
print('O valor total a pagar é de {}R$ {:.2f}{}.'.format('\033[1;34m', t, '\033[m'))
