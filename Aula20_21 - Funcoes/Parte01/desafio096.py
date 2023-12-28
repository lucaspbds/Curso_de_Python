# Função que calcula área
def areaDoTerreno(largura, comprimento):
    area = largura * comprimento
    print(f'A área de um terreno {largura} x {comprimento} é de {area:.1f} m².')


print('Controle de Terrenos')
print('-' * 20)
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
areaDoTerreno(largura, comprimento)
