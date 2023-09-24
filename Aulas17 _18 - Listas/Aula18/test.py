dados = list()
pessoas = [['Marcos', 19], ['Pedro', 25], ['João', 13]]
dados.append('Lucas')
dados.append(16)
pessoas.append(dados[:])
dados[0] = 'Maria'
dados[1] = 35
pessoas.append(dados[:])
print(pessoas)
for p in pessoas:
    print(p[0])
pessoas.clear()
print(pessoas)
