# Função para Fatorial
def fatorial(num, show=False):
    """
    => Função para calcular fatorial de um número.
    :param num: O número que será fatorado;
    :param show: (opcional) Mostrar ou não a conta;
    :return: O valor do fatorial de um número
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show:
            print(c, end='')
            if c != 1:
                print(' x ', end='')
            else:
                print(' = ', end='')

    return f


print(fatorial(6, True))
# help(fatorial)
