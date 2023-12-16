from random import randint

vitoria = True
soma = vitorias_jogador = 0

while vitoria:
    print('=' * 25)
    print('VAMOS JOGAR PAR OU ÍMPAR')
    print('=' * 25)
    jogador = int(input('Digite um valor[0 a 10]: '))
    computador = randint(0, 10)
    soma = jogador + computador
    tipo = input('Par ou Ímpar?[P/I] ').strip().upper()[0]
    while tipo not in 'PIÍ':
        tipo = input('Par ou Ímpar?[P/I] ').strip().upper()[0]
    if tipo == 'P':
        tipo_computador = 'I'
    else:
        tipo_computador = 'P'
    print(f'Você jogou {jogador} ({tipo}) e eu joguei {computador} ({tipo_computador}). '
          f'A soma foi {soma} e deu ', end='')
    if soma % 2 == 0:
        print('PAR')
        if tipo in 'P':
            vitorias_jogador += 1
            print('\033[32mVOCÊ GANHOU!\033[m\nVamos jogar novamente...\n')
        else:
            vitoria = False
    else:
        print('ÍMPAR')
        if tipo in 'ÍI':
            vitorias_jogador += 1
            print('\033[32mVOCÊ GANHOU!\033[m\nVamos jogar novamente...\n')
        else:
            vitoria = False
print('\033[31mVOCÊ PERDEU!')
print(f'\033[32mQtd de vitórias: {vitorias_jogador}')
