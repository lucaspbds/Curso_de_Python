# Número por Extenso
numero_extenso = (
    'Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve',
    'Thirteen',
    'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen', 'Twenty')
while True:
    num = int(input('Digite um número para saber o número por extenso [0 a 20]: '))
    while num < 0 or num > 20:
        print('\033[31mPor favor! Digite um número maior ou igual a 0 e menor ou igual a 20.\033[m')
        num = int(input('Digite um número para saber o número por extenso [0 a 20]: '))
    print(f'\033[34mO número {num} por extenso é {numero_extenso[num]}\033[m')
    r = input('Deseja continuar?[S/N] ').strip().upper()[0]
    if r == 'N':
        break
    print('-=-'*10)
print('\033[31mPrograma finalizado!')
