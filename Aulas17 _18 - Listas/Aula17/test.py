# lanche = ['pipoca', 'arroz', 'cookie', 'hamburguer']
# lanche.insert(1, 'Pão')
# lanche.pop()
# del lanche
#
# lista = list(range(4, 11, 2))
# print(lista)
# lista1 = [2, 2, 4, 1, 2, 2,0, 50]
# lista1.sort(reverse=True)
# print(lista1)
lista = [2, 2, 4, 1, 2, 2, 0, 50]
# for pos, num in enumerate(lista):
#     if num == 2:
#         del lista[pos]
print(lista.count(2))
while lista.count(2) != 0:
    for num in lista:
        if num == 2:
            lista.remove(num)
print(lista)
