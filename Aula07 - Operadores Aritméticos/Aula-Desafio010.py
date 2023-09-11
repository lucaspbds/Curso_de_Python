print('=-'*10+'Conversor de moedas(Dólar/Real)'+'-='*10)
while True:
    print('1 - Comprar Dólar \n2 - Comprar Real')
    tipo = input('Digite a opção que deseja: ')
    if tipo == '1' or tipo == '2':
        valor = float(input('Valor: '))
        if tipo == '1':
            print(f'Quant. de dólar que dar para comprar: US${valor / 3.27:.2f}')
        if tipo == '2':
            print(f'Quant. de real que dar para comprar: R${3.27 * valor}')
        break
    else:
        print('INVÁLIDO! Só pode colocar 1 ou 2.')