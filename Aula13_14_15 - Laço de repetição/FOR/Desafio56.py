print('-=-'*10+'Analisador completo'+'-=-'*10)
media_idade = 0
idade_maior = 0
cont_mulher = 0
nome_velho = ''
for i in range(1, 5):
    print('-'*5+f' {i}º Pessoa '+'-'*5)
    nome = input('Digite o seu nome: ').strip()
    idade = int(input('Digite a sua idade: '))
    sexo = input('Digite o seu sexo (M: Masc ou F: Fem): ').strip()
    media_idade += idade
    if i == 1 and sexo in 'Mm':
        idade_maior = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > idade_maior:
        idade_maior = idade
        nome_velho = nome
    if sexo == 'F' and idade < 20:
        cont_mulher += 1
media_idade = media_idade/4
print(f'Média das idades: {media_idade}')
print(f'Homem mais velho: {nome_velho} - {idade_maior} anos')
print(f'Qtd de mulheres com idade menor que 20 anos: {cont_mulher}')
