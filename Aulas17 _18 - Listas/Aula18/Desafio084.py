# Lista composta e análise de dados
pessoas = []
peso_maior = peso_menor = 0
nome_peso_maior = []
nome_peso_menor = []
while True:
    dados = []
    dados.append(input('Digite o seu nome: ').strip().capitalize())
    dados.append(float(input('Digite o seu peso (Kg): ').strip()))
    if len(pessoas) == 0:
        peso_maior = peso_menor = dados[1]
    else:
        if dados[1] > peso_maior:
            peso_maior = dados[1]
        elif dados[1] < peso_menor:
            peso_menor = dados[1]
    pessoas.append(dados[:])
    # dados.clear() Pode colocar isso também
    r = input('Deseja continuar?[S/N] ').strip()
    while r not in 'SsNn':
        print('\033[31mErro de digitação! Por favor, digite novamente...\033[m')
        r = input('Deseja continuar?[S/N] ').strip()[0]
    if r in 'Nn':
        break
print(f'Qtd de pessoas cadastradas: {len(pessoas)}')
print(f'O maior peso foi de {peso_maior}kg. Peso de ', end='')
for pessoa in pessoas:
    if pessoa[1] == peso_maior:
        print(f'[{pessoa[0]}]', end='  ')
print(f'\nO menor peso foi de {peso_menor}kg. Peso de ', end='')
for pessoa in pessoas:
    if pessoa[1] == peso_menor:
        print(f'[{pessoa[0]}]', end='  ')
