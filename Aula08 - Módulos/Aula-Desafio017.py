from math import hypot
print('-='*10+'Cateto e Hipotenusa'+'=-'*10)
catop = float(input('Cateto oposto: '))
catad = float(input('Cateto adjacente: '))
hipo = hypot(catad, catop)
print(f'Valor da hipotenusa: {hipo:.2f}')
