# Formatando Moedas em Python Parte 2
from utilidadesCeV import moeda, dado


preco = dado.leiaDinheiro("Digite o preço do produto: R$")
moeda.resumo(preco, 35, 22)
