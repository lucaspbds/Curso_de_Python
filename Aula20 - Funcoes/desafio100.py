# Funções para sortear e somar
from random import randint
from time import sleep

numbers = []


def sorteia():
    print('Sorteando os números... ', end='')
    for i in range(0, 5):
        numbers.append(randint(1, 10))
        print(numbers[i], end=' ')
        sleep(0.5)
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    for number in lista:
        if number % 2 == 0:
            soma += number
    print(f'A soma dos números pares da lista {numbers} é {soma}.')


sorteia()
somaPar(numbers)
