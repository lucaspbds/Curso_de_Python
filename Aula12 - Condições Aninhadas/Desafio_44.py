print('{:=^50}'.format(' Gerenciador de Pagamentos '))
valor = float(input('Valor do produto: '))
print('''
                FORMAS DE PAGAMENTO
[ 1 ] À vista dinheiro/cheque  [ 3 ] Em até 2x no cartão
[ 2 ] Á vista no cartão        [ 4 ] 3x ou mais no cartão
''')
op = input('Escolha o modo de pagamento: ')
if op == '1':
    valor = valor - (valor*0.1)
    print('Preço do produto com desconto de 10%: R${:.2f}'.format(valor))
elif op == '2':
    valor = valor - (valor*0.5)
    print('Preço do produto com desconto de 5%: R${:.2f}'.format(valor))
elif op == '3':
    valor_mensal = valor/2
    print('Não ganha desconto!\nPreço do produto: R${:.2f}.'.format(valor), end=' ')
    print('O produto será parcelado em 2x de R${:.2f}'.format(valor_mensal))
elif op == '4':
    parcela = int(input('Quantas parcelas? '))
    valor = valor + (valor*0.2)
    valor_mensal = valor/parcela
    print('Preço do produto com 20% de juros: R${:.2f}.'.format(valor), end=' ')
    print('O produto será parcelado em {}x de R${:.2f}'.format(parcela, valor_mensal))
else:
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')