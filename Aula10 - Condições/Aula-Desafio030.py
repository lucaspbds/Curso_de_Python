print('=-'*10+'Par ou Ímpar'+'-='*10)
numero = float(input('Digite um número: ').strip())
if numero % 2 == 0:
    print('O numero {} é PAR!'.format(numero))
else:
    print('O numero {} é ÍMPAR!'.format(numero))
