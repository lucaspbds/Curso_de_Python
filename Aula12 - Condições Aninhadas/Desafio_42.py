print('=-'*10+'Analisando Triângulos 2.0'+'-='*10)
reta1 = float(input('Reta 1: '))
reta2 = float(input('Reta 2: '))
reta3 = float(input('Reta 3: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta2 + reta1:
    print('Podem formar um triângulo!', end=' ')
    if reta1==reta2 and reta1==reta3:
        print('Inclusive, um triângulo equilátero.')
    elif reta1!=reta2 and reta1==reta3 or reta1!=reta3 and reta1==reta2:
        print('Inclusive, um triângulo isósceles.')
    else:
        print('Inclusive, um triângulo escaleno.')
else:
    print('Não podem formar um triângulo')