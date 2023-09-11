print('=-'*10+'Verificando as primeiras letras de um texto'+'-='*10)
nome = input('Nome da cidade: ').upper().split()
print('Começa com "Santo": {}'.format('SANTO' in nome[0]))
