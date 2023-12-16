# Super Progressão Aritmética v3.0
a1 = int(input('Digite o 1º termo da P.A: '))
razao = int(input('Digite a razão dessa P.A: '))
cont = 1
qtd_termos = 0
an = a1
novos_termos = 10
while novos_termos != 0:
    qtd_termos += novos_termos
    while cont <= qtd_termos:
        print(an, end=' ')
        an += razao
        cont += 1
    novos_termos = int(input('\nVocê deseja ver mais quantos termos dessa P.A? '))
print(f'Fim!\n Quantidade de termos mostrados: {qtd_termos}')
