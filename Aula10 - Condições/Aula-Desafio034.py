print('=-'*10+'Aumentos múltiplos'+'-='*10)
salario = float(input('Digite o seu salário: '))
if salario > 1250:
    novosalario = salario + (salario * 0.1)
    print('Seu salário antigo: R${:.2f} \nSalário novo com o aumento de 10%: R${:.2f}'.format(salario, novosalario))
else:
    novosalario = salario + (salario * 0.15)
    print('Seu salário antigo: R${:.2f} \nSalário novo com o aumento de 15%: R${:.2f}'.format(salario, novosalario))
