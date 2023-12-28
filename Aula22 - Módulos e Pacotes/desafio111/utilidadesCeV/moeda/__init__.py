def aumentar(preco=0, porcentagem=0, sit=True):
    valor = (preco + (preco * (porcentagem / 100)))
    if sit:
        return moeda(valor)
    return valor


def diminuir(preco=0, porcentagem=0, sit=True):
    valor = preco - (preco * (porcentagem / 100))
    if sit:
        return moeda(valor)
    return valor


def metade(preco=0, sit=True):
    valor = preco / 2
    if sit:
        return moeda(valor)
    return valor


def dobro(preco=0, sit=True):
    valor = preco * 2
    if sit:
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


def resumo(preco=0, taxaAumento=0, taxaReducao=0):
    print('-=-' * 10)
    print(f"{'RESUMO DO VALOR':^30}")
    print('-=-' * 10)
    print(f"{'Preço analisado:':<20}" + moeda(preco))
    print(f"{'Dobro do preço:':<20}" + dobro(preco))
    print(f"{'Metade do preço:':<20}" + metade(preco))
    msg = f"{taxaAumento}% de aumento:"
    print(f"{msg:<20}" + aumentar(preco, taxaAumento))
    msg = f"{taxaReducao}% de redução:"
    print(f'{msg:<20}' + diminuir(preco, taxaReducao))
    print('-=-' * 10)
