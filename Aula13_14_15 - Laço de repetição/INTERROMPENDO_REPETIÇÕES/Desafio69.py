tot18 = qtd_homem = qtd_mulher20 = 0
print('=' * 20)
print('CADASTRE UMA PESSOA')
print('=' * 20)
while True:
    idade = int(input('Digite a sua idade: '))
    sexo = input('Digite o seu sexo [M/F]: ').strip().upper()[0]
    while sexo not in 'MF':
        print('\033[31mErro de digitação! Por favor, escreva novamente.\033[m')
        sexo = input('Digite o seu sexo [M/F]: ').strip().upper()[0]
    print('=' * 20)
    r = input('Deseja continuar?[S/N] ').strip().upper()[0]
    while r not in 'SN':
        print('\033[31mErro de digitação! Por favor, escreva novamente.\033[m')
        r = input('Deseja continuar?[S/N] ').strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        qtd_homem += 1
    if sexo == 'F' and idade < 20:
        qtd_mulher20 += 1
    if r == 'N':
        break
print(f'Qtd de pessoas maiores de 18 anos: {tot18}')
print(f'Qtd de homem: {qtd_homem}')
print(f'Qtd de mulher menor que 20 anos: {qtd_mulher20}')
