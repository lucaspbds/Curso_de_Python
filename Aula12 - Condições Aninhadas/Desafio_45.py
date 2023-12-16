print('-=-'*10+'Jogo Pedra, Papel e Tesoura'+'-=-'*10)
from random import choice
from time import sleep
lista = ['Pedra', 'Papel', 'Tesoura']
pc = choice(lista)
print('''Vamos jogar...
[ 1 ] Pedra 
[ 2 ] Tesoura
[ 3 ]Papel 
''')
op = input('Digite a sua jogada: ')
print('Carregando...')
sleep(2)
print('-=-'*10)
if pc == 'Pedra':
    if op == '1':
        print('{}\nEMPATE!'.format(pc))
    elif op == '2':
        print('{}COMPUTADOR VENCE'.format(pc))
    elif op == '3':
        print('{}\nJOGADOR VENCE!'.format(pc))
    else:
        print('OPÇÃO INVÁLIDA. Tente novamente!')
elif pc == 'Papel':
    if op == '1':
        print('{}\nCOMPUTADOR VENCE!'.format(pc))
    elif op == '2':
        print('{}\nJOGADOR VENCE!'.format(pc))
    elif op == '3':
        print('{}\nEMPATE!'.format(pc))
    else:
        print('OPÇÃO INVÁLIDA. Tente novamente!')
elif pc == 'Tesoura':
    if op == '1':
        print('{}\nJOGADOR VENCE!'.format(pc))
    elif op == '2':
        print('{}\nEMPATE!'.format(pc))
    elif op == '3':
        print('{}\nCOMPUTADOR VENCE!'.format(pc))