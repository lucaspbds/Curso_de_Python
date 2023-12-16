print('=-'*10+'Custo de Viagem'+'-='*10)
distancia = float(input('Digite a distância percorrida: ').strip())
if distancia <= 200:
    print('Preço da passagem: R${:.2f}'.format(distancia*0.5))
else:
    print('Preço da passagem: R${:.2f}'.format(distancia*0.45))
