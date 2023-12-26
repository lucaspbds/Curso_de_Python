def teste(n2):
    global n1
    n1 = 8
    n2 += 4
    n3 = 2
    print(f'n1 dentro vale {n1}')
    print(f'n2 dentro vale {n2}')
    print(f'n3 dentro vale {n3}')


n1 = 5
teste(n1)
print(f'n1 fora vale {n1}')
