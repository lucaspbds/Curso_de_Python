valores = [2, 5, 3, 7, 14]


def dobrar(lista):
    index = 0
    while index < len(lista):
        lista[index] *= 2
        index += 1
    print(lista)


dobrar(valores[:])
print(valores)
