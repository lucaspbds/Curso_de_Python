# Tuplas com Times de Futebol
tabela_brasileirao = (
    'Botafogo', 'Palmeiras', 'Grêmio', 'Flamengo', 'Fluminense', 'Bragantino', 'Athlético-PR', 'Fortaleza',
    'Atlético-MG',
    'Cuiabá', 'São Paulo', 'Cruzeiro', 'Corithians', 'Internacional', 'Goiás', 'Bahia', 'Santos', 'Vasco da Gama',
    'América-MG', 'Coritiba')
print('Os 5 primeiros colocados do Brasileirão')
for pos, time in enumerate(tabela_brasileirao):
    if pos < 5:
        print(f'{pos+1}º - {time}')
print('='*100)
print(f'Os últimos 4 colocados da tabela: {tabela_brasileirao[-4:]}')
print('='*100)
print(f'Times em ordem alfabética: {sorted(tabela_brasileirao)}')
print('='*100)
print(f'Posição do Fortaleza na tabela do Brasileirão: {tabela_brasileirao.index("Fortaleza")+1}º posição')
