print('-=-'*10+'Números primos'+'-=-'*10)
num = int(input('Digite um número: '))
cont = 0
for i in range(1, num + 1):
    if num % i == 0:
        print('\033[33m', end='')
        cont += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(i), end=' ')
if cont == 2:
    print(f'\033[m\nÉ um número primo, pois foi divisível somente por {cont} números.')
else:
    print(f'\033[m\nNão é um número primo, pois foi divisível por {cont} números.')
