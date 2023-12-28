# Formatando Moedas em Python Parte 2
from utilidadesCeV.moeda import *

preco = float(input('Digite o preço do produto: R$').replace(',', '.').strip())
resumo(preco, 35, 22)
