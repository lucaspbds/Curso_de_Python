print('-='*10+'Calculando Descontos'+'=-'*10)
valor = float(input('Digite o preço do produto: '))
print('-='*20)
valornovo = valor - (valor*0.05)
print(f'Preço novo do produto com desconto de 5%: R${valornovo:.2f}')
