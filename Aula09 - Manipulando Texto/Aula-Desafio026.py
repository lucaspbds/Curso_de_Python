print('=-'*10+'Primeiro e última ocorrência de uma string'+'-='*10)
frase = input('Digite uma frase: ').upper().strip()
Quantdeletras = len(frase)-1
print('Quant. de vezes que aparece a letra "A" ou "a": {}'.format(frase.count('A')))
print('Posição que aparece a primeira letra "A" ou "a": {}'.format(frase.find('A')+1))
print('Posição que a letra "A" ou "a" apareceu pela última vez: {}'.format(frase.rfind('A')+1))
