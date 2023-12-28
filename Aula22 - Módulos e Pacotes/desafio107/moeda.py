def aumentar(preco, porcentagem=0, sit=True):
    valor = preco + (preco * (porcentagem / 100))
    return f'{valor:.2f}'


def diminuir(preco, porcentagem=0, sit=True):
    valor = preco - (preco * (porcentagem / 100))
    return f'{valor:.2f}'


def metade(preco, sit=True):
    valor = preco / 2
    return f'{valor:.2f}'


def dobro(preco, sit=True):
    valor = preco * 2
    return f'{valor:.2f}'

