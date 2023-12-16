alunos = []
boletim = {}
while True:
    boletim['nome'] = str(input('Nome: ')).strip().capitalize()
    boletim['media'] = float(input('Média: '))
    if boletim['media'] >= 6:
        boletim['situacao'] = 'Aprovado'
    else:
        boletim['situacao'] = 'Reprovado'
    alunos.append(boletim.copy())
    op = str(input('Deseja continuar?[S/N] ')).strip().upper()
    while op not in 'SN':
        print('\033[31mErro de digitação! Por favor, digite novamente...')
        op = str(input('Deseja continuar?[S/N] ')).strip().upper()
    if op == 'N':
        break
print('-=' * 30)
print('Nome           Média          Situação')
for boletim in alunos:
    print(f'{boletim["nome"]:<15}{boletim["media"]:<15}{boletim["situacao"]}')
