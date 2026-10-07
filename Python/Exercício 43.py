peso = float(input('Digite o seu peso em kilogramas: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso / (altura ** 2)
print('O seu imc é igual a {:.1f}:'.format(imc), end=' ')
if imc < 18.5:
    print('Você está abaixo do peso!')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal!')
elif 25 <= imc < 30:
    print('Você está com sobrepeso!')
elif 30 <= imc < 40:
    print('Você está com obesidade!')
# else:
elif imc >= 40:
    print('Você está com obesidade mórbida!')
