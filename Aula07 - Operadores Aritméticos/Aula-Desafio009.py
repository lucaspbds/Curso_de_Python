print('=-'*10+'Tabuada'+'-='*10)
while True:
    n1 = int(input('Qual tabuada você quer saber?'))
    print('-='*10)
    for i in range(0,12):
        print(f'{n1} x {i:2} = {n1*i}')
    print('-=' * 10)
    finalizar = input('Deseja continuar? S ou N').upper()
    if finalizar == 'N':
        break