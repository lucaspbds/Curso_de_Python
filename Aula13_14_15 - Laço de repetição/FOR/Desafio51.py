print('-=-'*10+'Progressão Aritmética'+'-=-'*10)
a1 = int(input('Digite o 1º termo: '))
r = int(input('Digite a razão dessa PA: '))
for n in range(1, 11):
    an = a1 + (n - 1) * r
    print(f'{an}', end=' → ')
print('Acabou')