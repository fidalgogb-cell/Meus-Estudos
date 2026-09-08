x = float(input('Digite um valor em metros:'))
a = x*100
b = x*1000
c = x/1000
print('O valor de {} metros equivale a {:.0f} centímetros, {:.0f} milímetros'.format(x,a,b),end= ' ')
# {:.0f} mostra como se fosse um número inteiro
print('e {:.0f} kilômetros.'.format(c))
