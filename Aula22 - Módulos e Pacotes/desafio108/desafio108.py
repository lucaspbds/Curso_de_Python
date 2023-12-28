# Formatando Moedas em Python
import moeda

preco = float(input('Digite o preço do produto: R$').replace(',', '.').strip())
print(f'A metade de {moeda.moeda(preco, "$")} é {moeda.moeda(moeda.metade(preco),"$")}.')
print(f'O dobro de {moeda.moeda(preco)} é de {moeda.moeda(moeda.dobro(preco))}')
print(f'Aumentando 10% de {moeda.moeda(preco)}, temos {moeda.moeda(moeda.aumentar(preco, 10))}.')
print(f'Diminuindo 13% de {moeda.moeda(preco)}, temos {moeda.moeda(moeda.diminuir(preco, 13))}.')
