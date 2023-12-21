pessoa = dict()
bd = list()
mediaDeIdade = 0
listaDeMulher = list()
listaDePessoas = list()
while True:
    pessoa.clear()
    pessoa["nome"] = input('Digite o seu nome: ').strip().capitalize()
    pessoa["sexo"] = input('Digite o seu sexo (M - Masculino e F - Feminino): ').strip().upper()[0]
    while pessoa["sexo"] not in "FM":
        print('Erro de digitação! Por favor, digite novamente!')
        pessoa["sexo"] = input('Digite o seu sexo (M - Masculino e F - Feminino): ').strip().upper()[0]
    pessoa["idade"] = int(input('Digite a sua idade: '))
    mediaDeIdade += pessoa["idade"]
    if pessoa["sexo"] == "F":
        listaDeMulher.append(pessoa["nome"])
    bd.append(pessoa.copy())
    op = input('Deseja continuar?S/N ').strip().upper()[0]
    while op not in 'SN':
        print('Erro de digitação! Por favor, digite novamente!')
        op = input('Deseja continuar?S/N ').strip().upper()[0]
    if op == 'N':
        break
qtdDePessoas = len(bd)
mediaDeIdade = mediaDeIdade / qtdDePessoas
for dado in bd:
    if dado["idade"] > mediaDeIdade:
        listaDePessoas.append(dado.copy())
print('-=-'*10)
print(f'Quantidade de pessoas cadastradas: {qtdDePessoas}')
print(f'Média de idade do grupo: {mediaDeIdade:5.2f}')
print('Mulheres cadastradas foram: ', end='')
if len(listaDeMulher) > 0:
    for mulher in listaDeMulher:
        print(mulher, end='  ')
else:
    print('0')
print('\nLista de pessoas que estão acima da idade média: ')
if len(listaDePessoas) > 0:
    for dado in listaDePessoas:
        print(f'  - Nome: {dado["nome"]}    Sexo: {dado["sexo"]}    Idade: {dado["idade"]}')
else:
    print('Não tem pessoas acima da idade média!')
print('\033[31m<<ENCERRADO>>\033[m')
