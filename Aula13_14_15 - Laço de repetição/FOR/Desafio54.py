from datetime import date
print('-=-'*10+'Grupo da Maioridade'+'-=-'*10)
maior_idade = 0
menor_idade = 0
ano_atual = date.today().year
for i in range(1, 8):
    ano = int(input(f'Digite o ano de nascimento da {i}º pessoa: '))
    idade = ano_atual - ano
    if idade >= 18:
        maior_idade += 1
    else:
        menor_idade += 1
print(f'Qtd pessoas com idade superior ou igual a 18 anos: {maior_idade} pessoa(s)')
print(f'Qtd pessoas com idade inferior a 18 anos: {menor_idade} pessoa(s)')
