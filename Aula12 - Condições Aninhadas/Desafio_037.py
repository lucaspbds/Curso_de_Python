print('-=-'*10+'Conversor de Bases Numéricas'+'-=-'*10)
num = int(input("Digite um número inteiro qualquer: "))
print('''Escolha uma das bases para conversão: 
[ 1 ] binário
[ 2 ] octal 
[ 3 ] hexadecimal
''')
op = input('Digite a sua escolha: ')
if op == '1':
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif op == '2':
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif op == '3':
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Valor inválido! Digite um valor que esteja no menu.')