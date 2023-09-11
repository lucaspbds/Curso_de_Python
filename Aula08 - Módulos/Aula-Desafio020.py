from random import shuffle
print('=-'*10+'Sorteando uma ordem na lista'+'-='*10)
aluno1 = input('Digite o nome do 1º aluno: ')
aluno2 = input('Digite o nome do 2º aluno: ')
aluno3 = input('Digite o nome do 3º aluno: ')
aluno4 = input('Digite o nome do 4º aluno: ')
alunos = [aluno1, aluno2, aluno3, aluno4]
shuffle(alunos)
print(f'Ordem das apresentações: {alunos}')
