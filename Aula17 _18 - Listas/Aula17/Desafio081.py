# Extraindo dados de uma Lista
valores = []

while True:
    valores.append(int(input('Digite um número: ')))
    r = input('Deseja continuar?[S/N] ').strip().upper()
    while r not in 'SN':
        print('Erro de digitação! Por favor, digite novamente...')
        r = input('Deseja continuar?[S/N] ').strip().upper()
    if r == 'N':
        break
valores.sort(reverse=True)
print(f'Qtd de números digitados: {len(valores)}')
print(f'Valores em ordem decrescente: {valores}')
if 5 in valores:
    print('O valor 5 está na(s) posição(ões): ', end='')
    for pos, num in enumerate(valores):
        if num == 5:
            print(pos, end=' ')
else:
    print('O valor 5 não está presente na lista!')
