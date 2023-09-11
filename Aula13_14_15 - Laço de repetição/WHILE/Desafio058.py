# Jogo da Adivinhação v2.0
from random import randint
from time import sleep

pc = randint(0, 10)
qtd_palpites = 1
acertou = False
print('Vamos jogar o jogo da adivinhação. Eu vou pensar em um número de 1 a 10 e você vai tentar adivinhar.')
print('Estou pensando em um número...')
sleep(2)
print('Pronto')
while not acertou:
    num = int(input('Em qual número eu pensei? '))
    if num != pc:
        qtd_palpites += 1
        print('\033[31mVocê errou! \033[mTente novamente...')
        if num < pc:
            print('Dica: É mais!\n')
        else:
            print('Dica: É menos\n')
    else:
        acertou = True
if qtd_palpites == 1:
    print(f'\033[32mParabéns! \033[mVocê acertou de primeira. O número que eu pensei foi {pc}.')
else:
    print(f'\033[32mParabéns! \033[mVocê acertou o número, mas precisou de {qtd_palpites} palpites para acertar.')
