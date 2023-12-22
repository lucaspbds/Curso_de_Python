def somar(*numbers):
    soma = 0
    for num in numbers:
        soma += num
    print(soma)


somar(2, 5, 10)
somar(2, 2)
somar(1)
