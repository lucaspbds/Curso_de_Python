# Formatando Moedas em Python Parte 2
from moeda import *

preco = float(input('Digite o preço do produto: R$').replace(',', '.').strip())
resumo(preco, 20, 0.0001)
