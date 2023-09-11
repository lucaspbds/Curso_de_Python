print('=-'*10+'Separando os dígitos de um número'+'-='*10)
n1 = int(input('Digite um valor: '))
Milhar = n1//1000
Centena = n1//100 % 10
Dezena = n1//10 % 10
Unidade = n1 % 10
print('Milhar: {}'.format(Milhar))
print('Centena: {}'.format(Centena))
print('Dezena: {}'.format(Dezena))
print('Unidade: {}'.format(Unidade))
