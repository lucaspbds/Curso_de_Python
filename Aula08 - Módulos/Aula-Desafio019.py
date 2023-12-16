from random import choice
print('=-'*10+'Sorteando um item na lista'+'-='*10)
aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digte o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')
print(f'Aluno sorteado: {choice([aluno1, aluno2, aluno3, aluno4])}')
