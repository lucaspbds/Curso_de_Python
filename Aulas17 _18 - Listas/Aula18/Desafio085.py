# Listas com pares e ímpares
valores = [[], []]
for i in range(0, 7):
    num = int(input(f'Digite o valor {i+1} inteiro: '))
    if num % 2 == 0:
        valores[0].append(num)

    else:
        valores[1].append(num)
valores[0].sort()
valores[1].sort()
print(f'Lista dos valores pares em ordem crescente: {valores[0]}')
print(f'Lista dos valores impares em ordem crescente: {valores[1]}')
