# Lista ordenada sem repetições
numbers = []
for i in range(0, 5):
    num = int(input(f'Digite um número: '))
    if i == 0 or num > numbers[-1]:
        numbers.append(num)
        print('Adicionado ao final da lista...')
    else:
        for pos, number in enumerate(numbers):
            if num < number:
                numbers.insert(pos, num)
                print(f'Adicionado na posição {pos}...')
                break
print(numbers)
