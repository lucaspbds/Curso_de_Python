# Boletim com listas compostas
boletim = []
media = soma = num = 0
while True:
    nome = (input('Nome: ').strip().capitalize())
    nota1 = (float(input('Nota 1: ')))
    nota2 = (float(input('Nota 2: ')))
    media = (nota1 + nota2) / 2
    boletim.append([nome, [nota1, nota2], media])
    r = input('Quer continuar?[S/N] ').strip().upper()[0]
    while r not in 'SN':
        print('\033[31mErro de digitação! Por favor, digite novamente...\033[m')
        r = input('Quer continuar?[S/N] ').strip().upper()[0]
    if r == 'N':
        break
print('-=' * 30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 25)
for pos, aluno in enumerate(boletim):
    print(f'{pos:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')
while num != 999:
    num = int(input('Mostrar notas de qual aluno?[999 - interrompe] '))
    print(f'Nome: {boletim[num][0]} - Notas: {boletim[num][1]}')
