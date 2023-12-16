# Cálculo do Fatorial
num = int(input('Digite um número para saber a fatorial desse número: '))
fatorial = 1
cont = num
print(f'{num}! = ', end='')
while cont > 0:
    print(cont, end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fatorial *= cont
    cont -= 1
print(fatorial)


# for i in range(1, num+1):
#     fatorial *= i
# print(f'{num}! = {fatorial}')
