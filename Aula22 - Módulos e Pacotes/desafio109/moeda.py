def aumentar(preco=0, porcentagem=0, formato=True):
    valor = (preco + (preco * (porcentagem / 100)))
    return moeda(valor) if formato is True else valor


def diminuir(preco=0, porcentagem=0, formato=True):
    valor = preco - (preco * (porcentagem / 100))
    if formato:
        return moeda(valor)
    return valor


def metade(preco=0, formato=True):
    valor = preco / 2
    if formato:
        return moeda(valor)
    return valor


def dobro(preco=0, formato=True):
    valor = preco * 2
    if formato:
        return moeda(valor)
    return valor


def moeda(preco=0, moeda="R$"):
    """
    -> Função que coloca um valor tipo float em uma formatação de moeda.
    :param preco: Recebe um valor tipo float e tem valor padrão 0;
    :param moeda: Recebe o tipo da moeda (R$, US$,...) e tem valor padrão R$;
    :return: Retorna uma string formatada.
    """
    if moeda == "US$" or moeda == "$":
        return f'{moeda}{preco:.2f}'
    return f'{moeda}{preco:.2f}'.replace('.', ',')
