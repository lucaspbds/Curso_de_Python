from time import sleep


def contador(inicio, fim, passo):
    """
    — > Faz uma contagem e mostra na tela.
    :param inicio: início da contagem
    :param fim: fim da contagem
    :param passo: passo da contagem
    :return: sem retorno

    Função criada por Lucas Pereira
    """
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


help(contador)
# contador(1, 10, 1)
# contador(10, 0, 2)
