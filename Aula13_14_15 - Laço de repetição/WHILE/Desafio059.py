# Criando um Menu de Opções
from time import sleep
op = '0'
n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))
while op != '5':
    print('''
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa
''')
    op = str(input('Digite a sua escolha: ')).strip()
    print('\033[33m')
    if op == '1':
        print(f'{n1} + {n2} = {n1 + n2}')
    elif op == '2':
        print(f'{n1} x {n2} = {n1 * n2}')
    elif op == '3':
        if n1 > n2:
            print(f'{n1} é maior que {n2}.')
        elif n1 < n2:
            print(f'{n2} é maior que {n1}.')
        else:
            print(f'Não tem como saber quem é o maior, porque são valores iguais.')

    elif op == '4':
        print('\033[mDigite os novos números...')
        n1 = int(input('Digite o 1º valor: '))
        n2 = int(input('Digite o 2º valor: '))
    elif op not in '12345':
        print('Opção inválida! Tente novamente...')
    print('\033[m')
    print('-=-' * 10)
    sleep(2)
print('\033[31mPrograma finalizado')
