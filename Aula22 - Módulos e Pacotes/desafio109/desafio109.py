# Formatando Moedas em Python Parte 2
import moeda

preco = float(input('Digite o preço do produto: R$').replace(',', '.').strip())

print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco)}.')
print(f'O dobro de {moeda.moeda(preco)} é de {moeda.dobro(preco)}.')
print(f'Aumentando 10% de {moeda.moeda(preco)}, temos {moeda.aumentar(preco, 10,False)}.')
print(f'Diminuindo 13% de {moeda.moeda(preco)}, temos {moeda.diminuir(preco, 13)}.')
