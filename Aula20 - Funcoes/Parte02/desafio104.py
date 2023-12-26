def leiaInt(texto):
    while True:
        num = input(texto)
        if num.isdecimal():
            return int(num)
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')


n = leiaInt('Digite um número inteiro: ')
print(f'Você acabou de digitar o número {n}.')
