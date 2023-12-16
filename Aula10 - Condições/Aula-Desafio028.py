from random import randint
from time import sleep
computador = randint(0, 5) #O computador vai sortear um número
print('-=-'*10+'Jogo da Adivinhação v1.0'+'-=-'*10)
print('Vou pensar um número entre 0 e 5... Tente adivinhar! =)')
jogador = int(input('Em que numero eu pensei? ').strip()) #Vai receber o número do jogador
print('-=-'*20)
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('VOCÊ ME VENCEU! =( \nNúmero sorteado foi {}'.format(computador))
else:
    print('VOCÊ PERDEU! \nEU GANHEI!!!;) \nNúmero sorteado foi {}'.format(computador))
