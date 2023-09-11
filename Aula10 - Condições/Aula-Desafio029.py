print('=-'*10+'Radar eletrônico'+'-='*10)
V = float(input('Velocidade do carro: ').strip())
if V > 80:
    multa = (V-80)*7
    print('Você foi multado! \nVocê deve pagar uma multa de R${:.2f}!'.format(multa))
else:
    print('Você está na velocidade correta! Abaixo do limite de velocidade (80 km/h).')
