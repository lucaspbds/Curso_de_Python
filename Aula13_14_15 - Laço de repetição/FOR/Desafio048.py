print('-=-'*10+'Soma ímpares múltiplos de três'+'-=-'*10)
soma = 0
cont = 0
for i in range(1, 501, 2):
    # 1, 3, 5, 7, 9, 11, 13, 15,...
    if i % 3 == 0:
        soma += i
        cont += 1

print(f'A soma dos {cont} números ímpares múltiplos de três: {soma}')
