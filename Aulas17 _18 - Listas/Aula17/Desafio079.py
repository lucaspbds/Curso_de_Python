# Valores únicos em uma Lista
numbers = []
while True:
    num = int(input('Digite um valor: '))
    if num not in numbers:
        numbers.append(num)
        print('\033[32mValor adicionado com sucesso!\033[m')
    else:
        print(f'\033[31mEsse número ({num}) já foi adicionado anteriormente.\033[m')
    r = input('Desja continuar?[S/N] ').strip().upper()
    while r not in 'SN':
        print('\033[31mErro de digitação! Digite um valor válido.\033[m')
        r = input('Desja continuar?[S/N] ').strip().upper()
    if r == 'N':
        break
numbers.sort()
print(f'Lista dos números digitados: {numbers}')
