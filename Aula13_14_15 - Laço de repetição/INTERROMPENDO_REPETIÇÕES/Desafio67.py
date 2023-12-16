tab = 1
while True:
    tab = int(input('Digite a tabuada que você quer saber: '))
    if tab < 0:
        break
    for i in range(1, 11):
        print(f'\033[32m{tab} x {i} = {tab * i}\033[m')
    print('\n' + '-=-' * 10 + '\n')
print('\033[31mPrograma finalizado')
