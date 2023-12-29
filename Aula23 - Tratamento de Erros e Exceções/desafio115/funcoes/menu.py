def menu(*opcoes, cor=False):
    for index, item in enumerate(opcoes):
        item = f'{item}'.capitalize()
        if cor:
            print(f'\033[1;32m{index + 1}\033[m - \033[36m{item}\033[m')
        else:
            print(f'{index + 1} - {item}'.title())
    print('-'*60)