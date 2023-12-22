# Função que descobre o maior
def maior(*numbers):
    maiorNumber = 0
    print('Analisando os valores passados...')
    print(f'Você passou {len(numbers)} número(s) => ', end='')
    for index, number in enumerate(numbers):
        print(number, end=' ')
        if index == 0:
            maiorNumber = number
        else:
            if number > maiorNumber:
                maiorNumber = number
    print('')
    print(f'O maior número foi {maiorNumber}')
    print('-=-' * 30)


maior(100, 50, 12, 5, 2)
maior(2)
maior(2, 5, 1, 4)
