print('-=-'*10+'Maior e menor da sequência'+'-=-'*10)
maior_peso = 0
menor_peso = 0
for i in range(1, 6):
    peso = float(input(f'Digite o peso da {i}º pessoa: '))
    if i == 1:
        menor_peso = maior_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso
print(f'Maior peso: {maior_peso}kg\nMenor peso: {menor_peso}kg')
