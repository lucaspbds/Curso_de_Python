# Palpites para a Mega Sena
from random import randint
from time import sleep
print('-'*20)
print(f"{'JOGA NA MEGA SENA':^20}")
print('-'*20)
palpites = []
jogada = []
qtd_jogos = int(input('Quantos jogos você quer que gere: '))
print('-=' * 10 + f'SORTEANDO {qtd_jogos} JOGOS' + '-=' * 10)
for jogo in range(0, qtd_jogos):
    for num in range(0, 6):
        numero = (randint(1, 60))
        if numero not in jogada:
            jogada.append(numero)
        else:
            continue  # Sortear outro número
    palpites.append(jogada[:])
    jogada.clear()
    sleep(1)
    palpites[jogo].sort()
    print(f'Jogo {jogo+1}: {palpites[jogo]}')
print('-='*10+f"{' < BOA SORTE! > ':^10}"+'-='*10)

