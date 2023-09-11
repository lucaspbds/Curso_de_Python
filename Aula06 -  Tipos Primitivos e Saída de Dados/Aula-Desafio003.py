dados = []
print('=-'*5+'Somar números'+'-='*5)
while True:
    dados.append(int(input('Digite um número: ')))
    finalizar = input('Deseja continuar? S ou N').upper()
    if finalizar == 'N':
        print(f'Soma dos números: {sum(dados)}')
        break


