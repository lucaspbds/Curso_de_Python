# Função de Contador
from time import sleep


def contador(inicio, fim, passo):
    print('-=-' * 20)
    print(f'Contagem de {inicio} até {fim}, de {passo} em {passo}:')
    if passo == 0:
        passo = 1
    if inicio < fim:
        if passo < 0:
            passo *= -1
        for i in range(inicio, fim + 1, passo):
            print(i, end=' ')
            sleep(0.5)
    else:
        if passo > 0:
            passo *= -1
        for i in range(inicio, fim - 1, passo):
            print(i, end=' ')
            sleep(0.5)
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)

print('-' * 60)
op = input('Você deseja que eu faça alguma contagem? ').strip().upper()[0]

if op == 'S':
    inicio = int(input('Início: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    contador(inicio, fim, passo)
else:
    print('\033[31m<<Programa encerrado>>')
