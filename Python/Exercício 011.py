l = float(input('Qual a largura da parede? '))
h = float(input('Qual a altura da parede? '))
a = l * h
print('A área da parede é de {}{:.2f} m²{}.'.format('\033[1;34m', a, '\033[m'))
# 2 m² = 1 l de tinta
x = a / 2
print('Você vai precisar de {}{:.2f} l{} de tinta.'.format('\033[1;34m', x, '\033[m'))
