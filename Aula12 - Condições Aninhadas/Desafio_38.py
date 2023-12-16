print('=-'*10+'Comparando números'+'-='*10)
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um outro número: '))
if n1>n2:
    print('O primeiro valor é maior!')
elif n2>n1:
    print('O segundo valor é maior!')
else:
    print('Não existe valor maior, os dois são iguais.')
