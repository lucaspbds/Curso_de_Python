media = cont = maior = menor = 0
r = 'S'
while r == 'S':
    num = int(input('Digite um número: '))
    media += num
    cont += 1
    if cont == 1:
        maior = menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num
    r = str(input('Deseja continuar?[S/N] ')).upper().strip()[0]
media = media / cont
print(f'Números digitados: {cont}')
print(f'Média dos números: {media:.2f}')
print(f'Maior número digitado: {maior}')
print(f'Menor número digitado: {menor}')

