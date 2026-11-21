soma = contador = 0
while True:
    num = int(input('Digite um número...ou 999 para parar! '))
    if num == 999:
        break
    soma += num
    contador += 1
print(f'A soma dos {contador} valores digitados é igual a {soma}')
