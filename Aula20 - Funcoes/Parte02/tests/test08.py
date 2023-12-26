def par(n=0):
    return n % 2 == 0


num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')
