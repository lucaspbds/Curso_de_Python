# Contando vogais em Tupla
palavras = ('banana', 'programar', 'curso', 'estudar', 'praticar')
for palavra in palavras:
    print(f'\nNa palavra \033[32m{palavra.upper()}\033[m temos ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(f'\033[33m{letra}\033[m', end=' ')
