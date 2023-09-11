# Progressão Aritmética v2.0
a1 = int(input('Digite o 1º termo da P.A: '))
r = int(input('Digite a razão dessa P.A: '))
cont = 1
an = a1
while cont <= 10:
    print(an, end=' - ')
    an += r
    cont += 1
print('FIM')
