# Maior e Menor valores na Lista
numeros = []
for i in range(0, 4):
    numeros.append(int(input(f'Digita um valor para a posição {i}: ')))
num_maior = max(numeros)
index_maior = numeros.index(num_maior)
num_menor = min(numeros)
index_menor = numeros.index(num_menor)
print(f'Número maior: {num_maior} - Posição: {index_maior}')
print(f'Número maior: {num_menor} - Posição: {index_menor}')
print(f'Lista dos números: {numeros}')
