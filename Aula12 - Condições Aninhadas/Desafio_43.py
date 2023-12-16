print('=-'*10+'Índice de Massa Corporal'+'-='*10)
peso = float(input('Digite o seu peso (kg): '))
alt = float(input('Digite a sua altura (m): '))
imc = peso / (alt ** 2)
if imc < 18.5:
    print('IMC: {:.2f}\nVocê está abaixo do peso!'.format(imc))
elif imc > 18.5 and imc < 25:
    print('IMC: {:.1f}\nVocê está no peso ideal!'.format(imc))
elif imc < 30:
    print('IMC: {:.1f}\nVocê está com sobrepeso!'.format(imc))
elif imc < 40:
    print('IMC: {:.1f}\nVocê está com obesidade!'.format(imc))
else:
    print('IMC: {:.1f}\nVocê está com obesidade mórbida!'.format(imc))
