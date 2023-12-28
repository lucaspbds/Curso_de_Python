# Exercitando módulos em Python
from moeda import *

preco = float(input('Digite o preço do produto: R$'))
print(f'A metade de R${preco:.2f} é R${metade(preco)}.')
print(f'O dobro de R${preco:.2f} é de R${dobro(preco)}')
print(f'Aumentando 10% de R${preco:.2f}, temos R${aumentar(preco,10)}.')
print(f'Diminuindo 13% de R${preco:.2f}, temos R${diminuir(preco, 13)}.')
