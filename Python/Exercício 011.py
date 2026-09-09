l = float(input('Qual a largura da parede?'))
h = float(input('Qual a altura da parede?'))
a = l*h
print('A área da parede é de {:.2f} metros quadrados'.format(a))
# 2 metros quadrados = 1 litro de tinta
x = a/2
print('Você vai precisar de {:.2f} litros de tinta.'.format(x))
