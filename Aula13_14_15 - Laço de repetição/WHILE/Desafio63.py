# Sequência de Fibonacci v1.0
qtd_termos = int(input('Digite a quantidade de números que você quer que apareça da sequência de Fibonacci: '))
cont = 3
anterior = 0
sucessor = 1
fibonacci = 0
print(f'{anterior} {sucessor}', end=' ')
while cont <= qtd_termos:
    # 0 1 1 2 3 5 8 13 ...
    fibonacci = anterior + sucessor
    anterior = sucessor
    sucessor = fibonacci
    print(fibonacci, end=' ')
    cont += 1
