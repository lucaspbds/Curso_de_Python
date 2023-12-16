print('-=-'*10+'Soma dos pares'+'-=-'*10)
soma = 0
cont = 0
for i in range(1, 6):
    num = int(input(f'Digite o número {i}º: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Você informou {cont} número(s) par(es) e a soma deles é {soma}.')
