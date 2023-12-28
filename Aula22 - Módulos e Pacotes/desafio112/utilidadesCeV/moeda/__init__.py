def aumentar(preco=0, porcentagem=0, sit=True):
    valor = (preco + (preco * (porcentagem / 100)))
    if sit:
        return moeda(valor)
    return f'\033[32m{valor}\033[m'


def diminuir(preco=0, porcentagem=0, sit=True):
    valor = preco - (preco * (porcentagem / 100))
    if sit:
        return moeda(valor)
    return f'\033[32m{valor}\033[m'


def metade(preco=0, sit=True):
    valor = preco / 2
    if sit:
        return moeda(valor)
    return f'\033[32m{valor}\033[m'


def dobro(preco=0, sit=True):
    valor = preco * 2
    if sit:
        return moeda(valor)
    return f'\033[32m{valor}\033[m'


def moeda(preco=0, moeda="R$"):
    """
    -> Função que coloca um valor tipo float em uma formatação de moeda.
    :param preco: Recebe um valor tipo float e tem valor padrão 0;
    :param moeda: Recebe o tipo da moeda (R$, US$,...) e tem valor padrão R$;
    :return: Retorna uma string formatada.
    """
    if moeda == "US$" or moeda == "$":
        return f'\033[32m{moeda}{preco:.2f}\033[m'
    return f'\033[32m{moeda}{preco:.2f}\033[m'.replace('.', ',')


def resumo(preco=0, taxaAumento=0, taxaReducao=0):
    print('\033[33m-=-\033[m' * 10)
    print(f"\033[1;34m{'RESUMO DO VALOR':^30}\033[m")
    print('\033[33m-=-\033[m' * 10)
    print(f"{'Preço analisado:':<20}" + moeda(preco))
    print(f"{'Dobro do preço:':<20}" + dobro(preco))
    print(f"{'Metade do preço:':<20}" + metade(preco))
    msg = f"{taxaAumento}% de aumento:"
    print(f"{msg:<20}" + aumentar(preco, taxaAumento))
    msg = f"{taxaReducao}% de redução:"
    print(f'{msg:<20}' + diminuir(preco, taxaReducao))
    print('\033[33m-=-\033[m' * 10)
