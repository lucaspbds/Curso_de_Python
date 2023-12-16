# Maior e Menor valores na Lista
numeros = []
for i in range(0, 5):
    numeros.append(int(input(f'Digita um valor para a posição {i}: ')))
num_maior = max(numeros)
index_maior = numeros.index(num_maior)
num_menor = min(numeros)
index_menor = numeros.index(num_menor)
print(f'Número maior: {num_maior} - Posição: ',end=' ')
for pos, num in enumerate(numeros):
    if num == num_maior:
        print(pos, end='... ')
print(f'\nNúmero menor: {num_menor} - Posição: ', end='')
for pos, num in enumerate(numeros):
    if num == num_menor:
        print(pos, end='... ')
print(f'\nLista dos números: {numeros}')
