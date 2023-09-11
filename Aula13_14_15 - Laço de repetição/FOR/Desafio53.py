print('-=-'*10+'Detector de Palíndromo'+'-=-'*10)
# frase = input('Digite uma frase: ').strip().upper()
# palavras = frase.split()
# junto = ''.join(palavras)
# inverso = ''
# for letra in range(len(junto) -1, -1, -1):
#     inverso += junto[letra]
# print(junto, inverso)
# if junto == inverso:
#     print('Temos um palíndromo!')
# else:
#     print('A frase digitada não é um palíndromo!')

#Outra forna de fazer

frase = input('Digite uma frase: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print(junto, inverso)
if junto == inverso:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
