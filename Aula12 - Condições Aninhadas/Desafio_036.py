print('-=-'*10+'Aprovando Empréstimo'+'-=-'*10)
valor_casa = float(input('Valor da casa: R$'))
salario = float(input('Salário: R$'))
anos = int(input('Com quantos anos você quer financiar a casa? '))
prestacao = valor_casa/(anos*12)
if prestacao <= salario*0.3:
    print('Empréstimo aprovado!\nPrestação: {:2f}'.format(prestacao))
else:
    print('Empréstimo negado!\nUltrapassou 30% do salário.\nPrestação: {:.2f}\n30% do salário: R${:.2f}'.format(prestacao,salario*0.3))
