# Ficha do Jogador
def ficha(nome="<desconhecido>", gols=0):
    print(f'O(A) jogador(a) {nome} fez {gols} gol(s) no campeonato.')


nome = input('Digite o nome do jogador: ').strip().capitalize()
qtdDeGols = input(f'Digite a quantidade de gols: ')
if qtdDeGols.isnumeric():
    qtdDeGols = int(qtdDeGols)
else:
    qtdDeGols = 0
if nome == '':
    ficha(gols=qtdDeGols)
else:
    ficha(nome, qtdDeGols)
