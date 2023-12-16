# Maior e menor valores em Tupla
from random import randint

numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
maior = sorted(numeros)[len(numeros) - 1]
menor = sorted(numeros)[0]
print(f'Valores sorteados: ', end='')
for num in numeros:
    print(num, end=' ')
print(f'\nO maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')
