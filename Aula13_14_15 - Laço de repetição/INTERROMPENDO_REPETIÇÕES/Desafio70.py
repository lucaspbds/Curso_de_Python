cont = preco_barato = total_gasto = produtos_maiores_1000 = 0
produto_barato = ' '
print('-=-' * 5)
print(f'LOJÃO DO LUCÃO')
print('-=-' * 5)
while True:
    nome_produto = input('Nome do produto: ').strip().upper()
    preco_produto = float(input('Preço do produto: R$'))
    cont += 1
    r = input('Deseja continuar?[S/N] ').strip().upper()[0]
    while r not in 'SN':
        print('\033[31mErro de digitação! Por favor, digite novamente.\033[m')
        r = input('Deseja continuar?[S/N] ').strip().upper()[0]
    total_gasto += preco_produto
    if cont == 1 or preco_produto < preco_barato:
        produto_barato = nome_produto
        preco_barato = preco_produto
    if preco_produto > 1000:
        produtos_maiores_1000 += 1
    if r == 'N':
        print('\033[31mPrograma finalizado!\033[m')
        break
print(f'Total gasto: R${total_gasto:.2f}')
print(f'Qtd de produtos que custam mais de R$1000.00: {produtos_maiores_1000}')
print(f'Produto mais barato\nNome: {produto_barato}\nPreço: R${preco_barato:.2f}')
