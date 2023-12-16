# Matriz em Python
matriz = [[], [], []]
for linha in range(0, 3):
    for coluna in range(0, 3):
        num = int(input(f'Digite um valor para a coluna [{coluna}, {linha}]: '))
        matriz[linha].append(num)
for linha in matriz:
    for coluna in linha:
        print(f'[ {coluna:^5} ]', end='')
    print()
