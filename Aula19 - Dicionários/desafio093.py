jogador = dict()
gols = list()
jogador['nome'] = input("Nome do jogador: ").strip().capitalize()
partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
for i in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {i}? ')))
jogador['gols'] = gols
jogador['totalGols'] = sum(gols)
print(f"O(A) jogador(a) {jogador['nome']} jogou {partidas} partidas.")
for index, gol in enumerate(jogador['gols']):
    print(f'     => Na partida {index}, fez {gol} gol(s).')
print(f"Foram um total de {jogador['totalGols']}")
