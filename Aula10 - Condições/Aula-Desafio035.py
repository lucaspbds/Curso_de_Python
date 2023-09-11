print('=-'*10+'Analisando Triângulos'+'-='*10)
reta1 = float(input('Reta 1: '))
reta2 = float(input('Reta 2: '))
reta3 = float(input('Reta 3: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta2 + reta1:
    print('Podem formar um triângulo!')
else:
    print('Não podem formar um triângulo')
