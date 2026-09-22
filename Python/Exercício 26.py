frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra {}A{} aparece {}{}{} vezes nessa frase.'.format('\033[1;31m', '\033[m', '\033[1;36m', frase.count('A'), '\033[m'))
print('A primeira letra {}A{} aparece na posição {}{}{}.'.format('\033[1;31m', '\033[m', '\033[1;36m', frase.find('A')+1, '\033[m'))
print('A última letra {}A{} aparece na posição {}{}{}.'.format('\033[1;31m', '\033[m', '\033[1;36m', frase.rfind('A')+1, '\033[m'))
