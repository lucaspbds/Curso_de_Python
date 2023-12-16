valores = []
num_par = []
num_impar = []
while True:
    valores.append(int(input('Digite um valor: ')))
    r = input('Deseja continuar?[S/N] ').strip().upper()
    while r not in 'SN':
        print('Erro de digitação! Por favor, digite novamente...')
        r = input('Deseja continuar?[S/N] ').strip().upper()
    if r == 'N':
        break
for num in valores:
    if num % 2 == 0:
        num_par.append(num)
    else:
        num_impar.append(num)
print('-=-'*10)
print(
    f'Lista dos valores digitados: {valores}\nLista dos números pares:{num_par}\nLista dos números ímpares: {num_impar}')
