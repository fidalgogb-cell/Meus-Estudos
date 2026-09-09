x = int(input('Digite um numero:'))
a = x*2
b = x*3
# c = x**(1/2)
c = pow (x,(1/2))
print('O dobro de {} é {}'.format(x,a))
print('O triplo de {} é {}'.format(x,b))
print('A raiz quadrada de {} é {:.2f}'.format(x,c))
