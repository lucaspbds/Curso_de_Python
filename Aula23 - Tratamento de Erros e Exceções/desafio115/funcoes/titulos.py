def titulo(texto, cor=False):
    texto = f'{texto}'.upper()
    if cor:
        print('-=-' * 20)
        print(f'\033[1;31m{texto:^60}\033[m')
        print('-=-' * 20)
    else:
        print('-=-' * 20)
        print(f'{texto:^60}')
        print('-=-' * 20)

# titulo('Menu Principal')
