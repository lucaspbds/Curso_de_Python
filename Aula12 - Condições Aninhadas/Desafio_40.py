print('=-'*10+'Média de notas'+'-='*10)
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1+nota2)/2
if media < 5.0:
    print('Reprovado!\nMédia({:.1f}) abaixo de 5.0.'.format(media))
elif media > 5.0 and media < 6.9:
    print('Recuperação!\nMédia({:.1f}) entre 5.0 e 6.9.'.format(media))
elif media >= 7:
    print('Aprovado!\nMédia({:.1f}) 7.0 ou superior.'.format(media))
