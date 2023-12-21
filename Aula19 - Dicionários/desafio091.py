# Jogo de Dados em Python
from random import randint
from time import sleep
from operator import itemgetter

jogadores = {}
cont = 1
for i in range(1, 5):
    jogadores[f"{i}"] = randint(1, 6)
    print(f"Jogador {i} - {jogadores[f'{i}']}")
    sleep(1)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for jogador in ranking:
    print(f'{cont}º LUGAR - Jogador {jogador[0]}')
    cont += 1

# Funciona também
#jogadores = {'jogador1': randint(1,6),
#             'jogador2': randint(1,6),
#             'jogador3': randint(1,6),
#             'jogador4': randint(1,6),
#             'jogador5': randint(1,6)
# }