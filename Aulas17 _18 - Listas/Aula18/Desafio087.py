# Mais sobre Matriz em Python
matriz = [[], [], []]
soma_pares = soma = maior = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        num = int(input(f'Digite um valor para a coluna [{linha}, {coluna}]: '))
        matriz[linha].append(num)
for linha in matriz:
    for coluna in linha:
        print(f'[ {coluna} ]', end='')
        if coluna % 2 == 0:
            soma_pares += coluna
        if linha.index(coluna) == 2:  # coluna 3
            soma += coluna
        if matriz.index(linha) == 1:  # segunda linha
            if linha.index(coluna) == 0:  # primeiro valor da linha
                maior = coluna
            elif coluna > maior:
                maior = coluna

    print('')
print(f'A soma dos valores pares é {soma_pares}.')
print(f'A soma dos valores da terceira coluna é {soma}.')
print(f'O maior valor da segunda linha é {maior}.')
