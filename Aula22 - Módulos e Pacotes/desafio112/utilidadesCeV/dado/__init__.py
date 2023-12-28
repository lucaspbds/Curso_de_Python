def leiaDinheiro(label):
    while True:
        preco = input(label).strip().replace(',', '.')
        valor = preco.replace('.', '')
        if valor.isnumeric():
            return float(preco)
        else:
            print(f'\033[31mErro: "{preco}" não é um valor válido! Digite um valor válido.\033[m')
