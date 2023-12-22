# Um print especial
txt = 'Curso Em Vídeo'


def titulo(texto):
    borda = 6
    qtdDeEspaco = borda // 2
    tamanho = len(texto) + borda
    print('-' * tamanho)
    print(' ' * qtdDeEspaco + f'{texto}')
    print('-' * tamanho)


titulo(txt)
