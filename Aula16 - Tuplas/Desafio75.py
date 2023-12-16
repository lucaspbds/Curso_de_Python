# Análise de dados em uma Tupla
cont = 0
numeros = (int(input('Digite um número: ')), int(input('Digite um outro número: ')), int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))

print(f'Números digitados: {numeros}')
print(f'Qtd de vezes que apareceu o valor 9: {numeros.count(9)} vez(es)')
if 3 in numeros:
    print(f'Posição que foi digitado o 1º valor 3: {numeros.index(3) + 1}º posição')
else:
    print('Não foi digitado nenhum valor 3!')
print(f'Números pares: ', end='')
for num in numeros:
    if num % 2 != 0:
        cont += 1
    else:
        print(num, end=' ')
    if cont == 4:
        print('NÃO TEM NÚMEROS PARES')
