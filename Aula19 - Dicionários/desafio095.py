jogador = dict()
jogadores = list()
gols = list()
codigo = 0
while True:
    print('-' * 30)
    jogador.clear()
    gols.clear()
    jogador['nome'] = input("Nome do jogador: ").strip().capitalize()
    partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    for i in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {i + 1}? ')))
    jogador['gols'] = gols[:]
    jogador['totalGols'] = sum(gols)
    jogadores.append(jogador.copy())
    op = input('Deseja continuar?S/N ').strip().capitalize()[0]
    while op not in "SN":
        print('Erro de digitação! Por favor, digite novamente.')
        op = input('Deseja continuar?S/N ').strip().capitalize()[0]
    if op == 'N':
        break
print('-=-' * 30)
print('   Cod Nome           Gols           Total')
for cod, jogador in enumerate(jogadores):
    print(f'{cod:>4}   ', end='')
    for dado in jogador.values():
        print(f'{str(dado):<15}', end='')
    print()
print('-' * 40)
while True:
    codigo = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if codigo == 999:
        break
    if codigo >= len(jogadores):
        print(f'ERRO! Não existe jogador com código {codigo}! Tente novamente')
    else:
        print('-- LEVANTAMENTO DO JOGADOR --')
        jogador = jogadores[codigo]
        print(f"O(A) jogador(a) {jogador['nome']} jogou {len(jogador['gols'])} partidas.")
        for partida, gol in enumerate(jogador['gols']):
            print(f'     => Na partida {partida + 1}, fez {gol} gol(s).')
        print(f"Foram um total de {jogador['totalGols']} gol(s).")
        print('-' * 30)

print('\033[31m<<ENCERRADO>>')
