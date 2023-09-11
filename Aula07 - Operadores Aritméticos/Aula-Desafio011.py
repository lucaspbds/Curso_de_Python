print('=-'*10+'Pintando Parede'+'-='*10)
larg = float(input('Largura da Parede (und: metro): '))
alt = float(input('Altura da Parede (und: metro): '))
area = larg * alt
print(f'Área da parede: {area}m² \nQuant. de tinta {area/2} L')