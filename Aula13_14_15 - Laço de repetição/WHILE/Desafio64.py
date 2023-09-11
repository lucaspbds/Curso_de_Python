# Tratando vários valores v1.0
num = cont = soma = 0
while num != 999:
    num = int(input('Digite um valor [Digite 999 para PARAR]: '))
    if num != 999:
        soma += num
        cont += 1
print(f'Números digitados: {cont}')
print(f'Valor da soma desses números: {soma}')

# outra maneira
# num = cont = soma = 0
# num = int(input('Digite um valor [Digite 999 para PARAR]: '))
# while num != 999:
#     soma += num
#     cont += 1
#     num = int(input('Digite um valor [Digite 999 para PARAR]: '))
# print(f'Números digitados: {cont}')
# print(f'Valor da soma desses números: {soma}')
