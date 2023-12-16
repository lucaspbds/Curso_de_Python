# Lista de Preços com Tupla
produtos = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.80,
            'Estojo', 15.00,
            'Livro', 35.00)
print('-' * 30)
print(f'\033[31m{"LISTAGEM DE PREÇO":^30}\033[m')
print('-' * 30)
for produto in range(0, len(produtos), 2):
    print(f'\033[34m{produtos[produto]:.<20}', end='')
    print(f'\033[32mR$ {produtos[produto + 1]:.2f}')
print('\033[m-' * 30)

# for produto in range(0, len(produtos)):
#     if produto % 2 == 0:
#         print(f'\033[34m{produtos[produto]:.<20}', end='')
#     else:
#         print(f'\033[32mR$ {produtos[produto]:.2f}')
